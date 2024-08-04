
import numpy as np

def initialize_board():
    return np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

def display_board(board):
    print(board)

def check_winner(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def tic_tac_toe():
    board = initialize_board()
    player = 'X'
    while True:
        display_board(board)
        try:
            row, col = map(int, input(f'Player {player}, enter row and column (0, 1, or 2): ').split())
            if row < 0 or row > 2 or col < 0 or col > 2:
                print('Invalid row or column! Please enter values between 0 and 2.')
                continue
            if board[row][col] == ' ':
                board[row][col] = player
                winner = check_winner(board)
                if winner:
                    display_board(board)
                    print(f'Player {winner} wins!')
                    break
                elif np.all(board != ' '):
                    display_board(board)
                    print('It's a draw!')
                    break
                player = 'O' if player == 'X' else 'X'
            else:
                print('Cell already taken!')
        except ValueError:
            print('Invalid input! Please enter row and column as two numbers separated by space.')
tic_tac_toe()
