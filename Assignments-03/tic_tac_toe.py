import random


# def drawBoard(board):
#     print(f'{board[7]} {board[8]} {board[9]}\n'
#           f'{board[4]} {board[5]} {board[6]}\n'
#           f'{board[1]} {board[2]} {board[3]}\n')


# def whoGoesFirst():
#     if random.randint(0, 1) == 0:
#         return 'computer'
#     else:
#         return 'player'
#

def makeMove(board, letter, move):
    board[move] = letter


def iswinner(bo, le):
    return ((bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
        return boardCopy


# def isSpaceFree(board, move):
#     return board[move] == ' '


# def getPlayerMove(board):
#     move = ' '
#     while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
#         print('What is your next move? (1-9)')
#     return input(int(move))


gameIsPlaying = True
while gameIsPlaying:
    board = ['_'] * 10
    letter = input('Do you want to be X or O?').upper()
    if letter == 'X':
        playerLetter = 'X'
        computerLetter = 'O'
    else:
        playerLetter = 'O'
        computerLetter = 'X'

    if random.randint(0, 1) == 0:
        turn = 'computer'
    else:
        turn = 'player'
    print('The ' + turn + ' will go first.')
    while gameIsPlaying:
        if turn == 'player':
            print(f'{board[7]} {board[8]} {board[9]}\n'
                  f'{board[4]} {board[5]} {board[6]}\n'
                  f'{board[1]} {board[2]} {board[3]}\n')
            move = ' '
            while move not in '1 2 3 4 5 6 7 8 9'.split() or not board[move] == ' ':
                move = int(input('What is your next move? (1-9)'))
                board[move] = letter
                print(f'{board[7]} {board[8]} {board[9]}\n'
                      f'{board[4]} {board[5]} {board[6]}\n'
                      f'{board[1]} {board[2]} {board[3]}\n')

                if ((board[1] == letter and board[2] == letter and board[3] == letter) or
                        (board[4] == letter and board[5] == letter and board[6] == letter) or
                        (board[7] == letter and board[8] == letter and board[9] == letter) or
                        (board[1] == letter and board[4] == letter and board[7] == letter) or
                        (board[2] == letter and board[5] == letter and board[8] == letter) or
                        (board[3] == letter and board[6] == letter and board[9] == letter) or
                        (board[1] == letter and board[5] == letter and board[9] == letter) or
                        (board[3] == letter and board[5] == letter and board[7] == letter)):
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                    break
                else:
                    break
