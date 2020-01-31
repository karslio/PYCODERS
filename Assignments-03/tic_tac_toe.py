board = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']


def show_board():
    print(f'{board[1]} {board[2]} {board[3]}\n'
          f'{board[4]} {board[5]} {board[6]}\n'
          f'{board[7]} {board[8]} {board[9]}\n')


while True:
    show_board()
    user = int(input('enter value'))
    board[user] = 'X'
    if (board[1] == "X" and board[2] == "X" and board[3] == "X") or \
            (board[4] == "X" and board[5] == "X" and board[6] == "X") or \
            (board[7] == "X" and board[8] == "X" and board[9] == "X") or \
            (board[1] == "X" and board[4] == "X" and board[7] == "X") or \
            (board[2] == "X" and board[5] == "X" and board[8] == "X") or \
            (board[3] == "X" and board[6] == "X" and board[9] == "X") or \
            (board[1] == "X" and board[5] == "X" and board[9] == "X") or \
            (board[3] == "X" and board[5] == "X" and board[7] == "X"):
        print('X win')
        break
    if (board[1] == "O" and board[2] == "O" and board[3] == "O") or \
            (board[4] == "O" and board[5] == "O" and board[6] == "O") or \
            (board[7] == "O" and board[8] == "O" and board[9] == "O") or \
            (board[1] == "O" and board[4] == "O" and board[7] == "O") or \
            (board[2] == "O" and board[5] == "O" and board[8] == "O") or \
            (board[3] == "O" and board[6] == "O" and board[9] == "O") or \
            (board[1] == "O" and board[5] == "O" and board[9] == "O") or \
            (board[3] == "O" and board[5] == "O" and board[7] == "O"):
        print('O win')
        break
