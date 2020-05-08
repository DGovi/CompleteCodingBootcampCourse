
##################################TICTACTOE###################################
# - 2 players should be able to play the game on this computer 
# - the board is printed out everythime a player makes a move
# - you should be able to accept input of the player position and then plaace a symbol 
#   on the board
# 
# use iof a number pad to place x and o
##############################################################################

print("Lets play TICTACTOE \n" );
print("player1 is x");
print("player2 is o")
print()

def displayBoard(board):
	print(board[1] + "|" + board[2] + "|" + board [3] + "				" + "1" + "|" + "2" + "|" + "3")
	print("-----				-----")
	print(board[4] + "|" + board[5] + "|" + board [6] + "				" + "4" + "|" + "5" + "|" + "6")
	print("-----				-----")
	print(board[7] + "|" + board[8] + "|" + board [9] + "				" + "7" + "|" + "8" + "|" + "9")


currentBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

gameIsFinished = False;

while gameIsFinished == False:
	displayBoard(currentBoard)
	player1Input = int(input("where would you like to place your symbol"))

	currentBoard[player1Input] = 'x'
	displayBoard(currentBoard)
	break