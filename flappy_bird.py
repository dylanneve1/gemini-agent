
import curses
import random

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    bird_y = sh // 2
    bird_x = sw // 4
    score = 0
    bird = 'o'
    game_over = False
    walls = []
    wall_speed = 1

    def create_wall():
        height = random.randint(1, sh - 2)
        return (height, sw)

    for _ in range(5):
        walls.append(create_wall())

    while not game_over:
        w.clear()

        for wall in walls:
            # Move wall towards the bird
            wall[1] -= wall_speed
            if wall[1] < 1:
                walls.remove(wall)
                score += 1  # Increment score for passing a wall
            if wall[1] < sw and wall[0] < sh:
                w.addstr(wall[0], wall[1], '|')
                if wall[1] == bird_x:
                    if bird_y == wall[0]:
                        game_over = True

        if bird_y < sh and bird_y >= 0:
            w.addstr(bird_y, bird_x, bird)

        w.addstr(0, 2, f'Score: {score}')
        w.refresh()

        key = w.getch()
        if key == curses.KEY_UP and bird_y > 0:
            bird_y -= 1
        elif key == curses.KEY_DOWN and bird_y < sh - 1:
            bird_y += 1
        if key == ord('q'):
            break

        # Generate new wall
        if len(walls) < 5:
            walls.append(create_wall())

    curses.endwin()

curses.wrapper(main)
