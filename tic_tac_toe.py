import random

the_board = [' ']*10


def displayBoard(board):

    print('\n'*100)
    print(''+board[7] + '|' + board[8] + '|' + board[9])
    print('------')
    print(''+board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(''+board[1] + '|' + board[2] + '|' + board[3])


def playerInput():
    marker = ''
    while marker != 'x' or marker != 'o':
        marker = input('Please choose a marker from X and O\n').upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')


def placeMarker(board, marker, position):
    board[position] = marker


def winCheck(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))  # d


def chooseFirst():
    if random.randint(0, 1) == 0:
        return 'Player2'
    else:
        return 'Player1'


def spaceCheck(board, position):
    return board[position] == ' '


def fullBoardCheck(board):
    for i in range(1, 10):
        if spaceCheck(board, i):
            return False
        
    return True


def playerChoice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not spaceCheck(board, position):
        position = int(input('Choose your next position: (1-9) '))
        return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')
while True:
    the_board = [' ']*10
    player1_marker, player2_marker = playerInput()
    turn = chooseFirst()
    print(turn + '\t will go the first')

    play_game = input('Are you ready to play the game? Y or N\n')

    if play_game.lower()[0] == 'y':
        game_on = True

    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            displayBoard(the_board)
            position = playerChoice(the_board)
            placeMarker(the_board, player1_marker, position)

            if winCheck(the_board, player1_marker):
                displayBoard(the_board)
                print('Congratulation!!! You won')
                game_on = False
            else:
                if fullBoardCheck(the_board):
                    displayBoard(the_board)
                    print('TIE GAME')
                    game_on = False

                else:
                    turn = 'Player2'
        else:
            displayBoard(the_board)
            position = playerChoice(the_board)
            placeMarker(the_board, player2_marker, position)

            if winCheck(the_board, player2_marker):
                displayBoard(the_board)
                print('Congratulations!!! You won')

            else:
                if fullBoardCheck(the_board):
                    displayBoard(the_board)
                    print('TIE GAME')
                    game_on = False

                else:
                    turn = 'Player1'

    if not replay():
        break
