################################## TICTACTOE ###################################
# - 2 players should be able to play the game on this computer
# - the board is printed out everythime a player makes a move
# - you should be able to accept input of the player position and then plaace a symbol
#   on the board
#
# use of a number pad to place x and o
##############################################################################
##############################################################################
#
# To run on sublime text, make sure REPL is installed,
# PRESS CMD+ALT+B on sublimetext to run it
#
#
#
#
##############################################################################
currentBoard = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
gameIsFinished = False
turn = 0
playAgain = False


def chose_game_mode():
    print("Lets play TICTACTOE \n")
    game_mode = int(input(
        "which game mode are you playing? \n 1-Player vs Player? \n 2-Player vs Computer?\n (enter 1 or 2)"))
    if game_mode == 1:
        print("PVP CHOSEN")
        print("player 1 is x")
        print("player 2 is o \n")
        pvp()
    elif game_mode == 2:
        pass
##########################################################


def pvp():  # player vs player
    displayBoard(currentBoard)
    playGame()

    while playAgain:
        playGame()
    print("Exiting TICTACTOE........")


'''
def pvc():
    print("VS COMPUTER CHOSEN")
    print("you go first")
'''


def displayBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")


def playGame():
    global gameIsFinished, turn, playAgain, currentBoard
    currentBoard = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gameIsFinished = False
    turn = 0
    playAgain = False

    while not gameIsFinished:
        thisTurn(currentBoard)
        gameIsFinished = isWinningMove(currentBoard) or turn == 8
        if turn == 8:
            print("game is tied")
        turn += 1
        displayBoard(currentBoard)
    playAgain = input("play Again? (\'y\' if yes, anything else for no)")
    if playAgain == 'y':
        playAgain = True
    else:
        playAgain = False


def thisTurn(board):
    if turn % 2 == 0:
        print("Player 1 turn!")
        player_input = ensure_valid_position(board)
        currentBoard[player_input] = 'x'
    else:
        print("Player 2 turn!")
        player_input = ensure_valid_position(board)
        currentBoard[player_input] = 'o'
    player_input = None


def ensure_valid_position(board):
    while True:
        try:
            playerInput = int(
                input("Which position (enter int between 1 and 9) \n"))
            if (playerInput < 1 or playerInput > 9):
                raise Exception
            elif (board[playerInput] == 'x' or board[playerInput] == 'o'):
                raise Exception
            else:
                return playerInput
        except:
            print("Enter a vaild number")
            continue


def isWinningMove(board):
    # check winning possibilities
    if (board[1] == board[2] == board[3]
        or board[4] == board[5] == board[6]
        or board[7] == board[8] == board[9]
        or board[1] == board[4] == board[7]
        or board[2] == board[5] == board[8]
        or board[3] == board[6] == board[9]
        or board[1] == board[5] == board[9]
            or board[3] == board[5] == board[7]):

        print("winner!!")
        return True
    else:
        return False


pvp()
