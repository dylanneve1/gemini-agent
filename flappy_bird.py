
import curses
import random

stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initial game variables
bird_y = sh // 2
bird_x = sw // 4
score = 0
bird = 'o'
game_over = False
walls = []

# Create initial walls
for i in range(5):
    height = random.randint(1, sh // 2)
    walls.append((height, sw + i * 20))

while not game_over:
    w.clear()
    
    # Draw walls
    for wall in walls:
        w.addstr(0, wall[1], '|')
        if wall[1] == bird_x:
            if bird_y == wall[0]:
                game_over = True
    
    # Move bird
    w.addstr(bird_y, bird_x, bird)
    # Check score
    if random.randint(0, 20) == 0:
        score += 1
    w.addstr(0, 2, f'Score: {score}')
    w.refresh()

    key = w.getch()
    if key == curses.KEY_UP and bird_y > 0:
        bird_y -= 1
    elif key == curses.KEY_DOWN and bird_y < sh - 1:
        bird_y += 1
    if key == ord('q'):
        break

curses.endwin()
