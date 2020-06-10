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
import random

currentBoard = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
gameIsFinished = False
turn = 0
playAgain = True
game_mode = None


def chose_game_mode():
    print("Lets play TICTACTOE \n")
    global game_mode
    while True:
        try:
            game_mode = int(input(
                "which game mode are you playing? \n 1-Player vs Player? \n 2-Player vs Computer?\n (enter 1 or 2)"))
            if game_mode == 1:
                print("PVP CHOSEN")
                print("player 1 is x")
                print("player 2 is o \n")
                playGame()
            elif game_mode == 2:
                print("PVC CHOSEN")
                print("you are x")
                playGame()
            else:
                raise Exception
            break
        except:
            print("enter 1 or 2")
            continue


def displayBoard(board):
    print("   " + board[1] + "   |   " + board[2] + "   |   " + board[3])
    print("-----------------------")
    print("   " + board[4] + "   |   " + board[5] + "   |   " + board[6])
    print("-----------------------")
    print("   " + board[7] + "   |   " + board[8] + "   |   " + board[9])
    print("\n")


def playGame():
    global turn, currentBoard, playAgain
    displayBoard(currentBoard)
    while playAgain:

        # new game
        currentBoard = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        gameIsFinished = False
        turn = 0
        playAgain = True

        # game loop
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
    print("Exiting TICTACTOE........")


def thisTurn(board):
    if turn % 2 == 0:
        print("Player 1 turn!")
        player_input = ensure_valid_position(board)
        board[player_input] = 'x'
    else:
        if game_mode == 1:
            print("Player 2 turn!")
            player_input = ensure_valid_position(board)
            board[player_input] = 'o'
        else:
            print("computer turn")
            computer_turn(board)


def computer_turn(board):

    available_positions = []
    for position in board:
        if position != "x" and position != "o" and position != "0":
            available_positions.append(position)
    rand_num = random.randint(0, len(available_positions))
    board[int(available_positions[rand_num])] = "o"


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
            print("Enter a VALID number")
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


chose_game_mode()
