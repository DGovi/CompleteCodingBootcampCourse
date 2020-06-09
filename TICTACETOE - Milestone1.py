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
currentBoard = ["0", " ", " ", " ", " ", " ", " ", " ", " ", " "]
gameIsFinished = False
turn = 0
playAgain = False

print("Lets play TICTACTOE \n")
print("player 1 is x")
print("player 2 is o \n")


def newGame():
    global currentBoard, gameIsFinished, turn, playAgain
    currentBoard = ["0", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    gameIsFinished = False
    turn = 0
    playAgain = False
    return True


def displayBoard(board):
    print("1|2|3    " + board[1] + "|" + board[2] + "|" + board[3])
    print("-----    -----")
    print("4|5|6    " + board[4] + "|" + board[5] + "|" + board[6])
    print("-----    -----")
    print("7|8|9    " + board[7] + "|" + board[8] + "|" + board[9])
    print("\n")


def playGame():
    global gameIsFinished, turn, playAgain, currentBoard
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
    while True:
        try:
            if turn % 2 == 0:
                print("Player 1 turn!")
                player1Input = int(
                    input("where would you like to place your x (enter int between 1 and 9) \n"))
                if (player1Input < 1 or player1Input > 9):
                    raise Exception
                elif (board[player1Input] == 'x' or board[player1Input] == 'o'):
                    raise Exception
                else:
                    currentBoard[player1Input] = 'x'
            else:
                print("Player 2 turn!")
                player2Input = int(
                    input("where would you like to place your o (enter int between 1 and 9) \n"))
                if (player1Input < 1 or player1Input > 9):
                    raise Exception
                elif (board[player1Input] == 'x' or board[player1Input] == 'o'):
                    raise Exception
                else:
                    currentBoard[player2Input] = 'o'
            break
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
        # check if positinos are board spaces
        if(board[1] == " " or board[2] == " " or board[3] == " " or board[4] == " " or board[7] == " " or board[9] == " "):
            return False
        print("youve won!!")
        return True
    else:
        return False


def isMoveAllowed(position, board):
    if (position < 1 or position > 9 or board[position] == 'x' or board[position] == 'o'):
        return False
    return True


# game start
newGame()
displayBoard(currentBoard)
playGame()

while playAgain:
    newGame()
    playGame()
print("Exiting TICTACTOE........")
