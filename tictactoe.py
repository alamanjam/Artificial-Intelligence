import random
class tictactoe:
	def __init__(self, mark):
		self.board= "123456789"
		self.mark = mark
		self.winningmark = ""
		if self.mark == "X":
			self.cpuMark = "O"
		else:
			self.cpuMark = "X"
	def move(self):
		giffick
	def goalTest(self): 
		return ((self.board[1] == self.board[2] == self.board[3])) or # across the top
    	((self.board[4] == self.board[5] == self.board[6]) or # across the middle
    	((self.board[7] == self.board[8] == self.board[9]) or # across the bottom
    	((self.board[1] == self.board[4] == self.board[7]) or # down the left side
    	((self.board[2] == self.board[5] == self.board[8]) or # down the middle
    	((self.board[3] == self.board[6] == self.board[9]) or # down the right side
    	((self.board[1] == self.board[5] == self.board[9]) or # diagonal
    	((self.board[3] == self.board[5] == self.board[7]) # diagonal
    	return False 
	def display(self, num):
		print("Move " + str(num))
		for m in range(0, 3):
			print(self.matrix[m])
mark = input("Do you want X or O? ")
t = tictactoe(mark)
for x in range(0, 9):
	if(t.goalTest()==True):
		break
	t.display(x)
	t.move()
	t.display(x+1)
	t.cpuMove()
print(t.winningmark + " wins!")


