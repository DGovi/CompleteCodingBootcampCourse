
################################## TICTACTOE ###################################
# - 2 players should be able to play the game on this computer
# - the board is printed out everythime a player makes a move
# - you should be able to accept input of the player position and then plaace a symbol
#   on the board
#
# use of a number pad to place x and o
##############################################################################
##############################################################################
# IMPORTANT
#
#
# on sublime text, make sure repl is installed,
# PRESS CMD+ALT+B on sublimetexte to run it
#
#
#
#
##############################################################################

currentBoard = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
gameIsFinished = False
turn = 0
playAgain = False

print("Lets play TICTACTOE \n")
print("player 1 is x")
print("player 2 is o \n")


def displayBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")


def isWinningMove(board):
    # check the rows
    if (board[1] == board[2] == board[3] or
        board[4] == board[5] == board[6] or
        board[7] == board[8] == board[9] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[3] == board[6] == board[9] or
        board[1] == board[5] == board[9] or
            board[3] == board[5] == board[7]):
        print("youve won!!")
        return True
    else:
        return False


def isMoveAllowed(position, board):

    if (position < 1 or position > 9 or board[position] == 'x' or board[position] == 'o'):
        return False
    return True


def thisTurn():
    while True:
        try:
            if turn % 2 == 0:
                print("Player 1 turn!")
                player1Input = int(
                    input("where would you like to place your x (enter int between 1 and 9) \n"))
                currentBoard[player1Input] = 'x'
            else:
                print("Player 2 turn!")
                player2Input = int(
                    input("where would you like to place your o (enter int between 1 and 9) \n"))
                currentBoard[player2Input] = 'o'
            break
        except:
            print("try again with a valid number this time")
            continue


def playGame():
    global gameIsFinished, turn, playAgain
    while not gameIsFinished:
        thisTurn()
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


def newGame():
    global currentBoard, gameIsFinished, turn, playAgain
    currentBoard = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gameIsFinished = False
    turn = 0
    playAgain = False
    return True


# game start
newGame()
displayBoard(currentBoard)
playGame()

while playAgain:
    newGame()
    playGame()
print("Exiting TICTACTOE........")
