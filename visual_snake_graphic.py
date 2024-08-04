sh, sw = 20, 40  # Static height and width for the graphic
snake = [[sh//2, sw//4], [sh//2, sw//4-1], [sh//2, sw//4-2]]

# Initialize a blank board
board = [[' ' for _ in range(sw)] for _ in range(sh)]

# Draw the snake on the board
for segment in snake:
    y, x = segment
    board[y][x] = 'O'  # Use 'O' to represent the snake

# Create a string representation of the board
graphic = '\n'.join([''.join(row) for row in board])
print(graphic)

