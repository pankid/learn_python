from random import randint

board = []

for x in range(0,5):
	board.append(["W"] * 5)

def print_board(board):
	for row in board:
		print " ".join(row)

print_board(board)

def random_row(board):
	return randint(0, len(board) -1)

def random_col(board):
	return randint(0, len(board) -1)

ship_row = random_row(board)
ship_col = random_col(board)




for turn in range(4):
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))


	print ship_row
	print ship_col

	print "Turn", turn + 1
	if guess_row == ship_row and guess_col == ship_col:
		print "Congratulations?"
		break	
	else:
			
		if (guess_row not in range(5)) or (guess_col not in range(5)):
			print "NAH"
		elif (board[guess_row][guess_col] == "X"):
			print "NOT AGAIN"
		else:
			board[guess_row][guess_col] = "X"
			print "missed me" 
			print_board(board)

		if (turn == 3):
			print "Game Over"
