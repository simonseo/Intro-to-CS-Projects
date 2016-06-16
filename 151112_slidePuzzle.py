import random
import os

class Tile:
	def __init__(self, row, col, val = 'E'):
		self.row = row
		self.col = col
		self.val = val
		
class Board:
	def __init__(self, numRow, numCol):
		self.numRow = numRow
		self.numCol = numCol
		self.board = []
		self.azimList = [(-1,0),(0,1),(1,0),(0,-1)]
		self.createBoard()
	
	def __str__(self):
		tmp = ''

		#for col in range(self.numCol):
		#	tmp += '\t\t'+str(col)
		tmp += '\n\t' + '+-------'*(self.numCol) + '+'
		tmp += '\n'

		for row in range(self.numRow):
			tmp += '\t|\t'

			for col in range(self.numCol):
				tmp += str(self.getTilerc(row, col).val)+'\t|\t'
			tmp += '\n\t' + '+-------'*(self.numCol) + '+'
			tmp +='\n'
		return(tmp)

	def createBoard(self):		
		for row in range(self.numRow):
			for col in range(self.numCol):
				if row == self.numRow-1 and col == self.numCol-1:
					self.board.append(Tile(row, col))
				else:
					self.board.append(Tile(row, col, 1 + row*self.numCol + col))

	def move(self, inputval, mode = 'c'):
		"""azim: range(4) moves empty space; dir=(1up(-1,0),2right(0,+1),3down(+1,0),4left(0,-1))"""
		azim = inputval
		if mode == 'u':
			if inputval.lower() == '8':
				azim = 0
			elif inputval.lower() == '6':
				azim = 1
			elif inputval.lower() == '2':
				azim = 2
			elif inputval.lower() == '4':
				azim = 3
		
		targetRow = self.getTileval('E').row + self.azimList[azim][0]
		targetCol = self.getTileval('E').col + self.azimList[azim][1]
		self.getTileval('E').val = self.getTilerc(targetRow, targetCol).val
		self.getTilerc(targetRow,targetCol).val = 'E'

	def checkWin(self):
		win = True
		count = 1
		for row in range(self.numRow):
			for col in range(self.numCol):
				if not(row == self.numRow-1 and col == self.numCol-1) and self.getTilerc(row, col).val != count:
					win = False
				count += 1
		return win

	def getTilerc(self, row, col):
		for tile in self.board:
			if tile.row == row and tile.col == col:
				return tile

	def getTileval(self, val):
		for tile in self.board:
			if tile.val == val:
				return tile

	def shuffle(self, num):
		for i in range(num):
			rand = random.randint(0,3)
			while not (0 <= self.getTileval('E').row + self.azimList[rand][0] < self.numRow and 0 <= self.getTileval('E').col + self.azimList[rand][1] < self.numCol):
				rand = random.randint(0,3)
			self.move(rand)
			
	def play(self):
		while not self.checkWin():
			os.system('cls')
			print(self)
			inputVal = input('Keys:\n  8\n4   6\n  2\ninput: ')
			while (inputVal not in ['2', '4', '6', '8']) or\
				(inputVal == '8' and self.getTileval('E').row == 0) or\
				(inputVal == '4' and self.getTileval('E').col == 0) or\
				(inputVal == '6' and self.getTileval('E').row == self.numRow-1) or\
				(inputVal == '2' and self.getTileval('E').col == self.numCol-1):
				inputVal = input('Keys:\n  8\n4   6\n  2\ninput: ')
			self.move(inputVal, 'u')
		
		print(self)
		print('\nYou won!!')
		
b = Board(4,4)
print(b)
b.shuffle(101)
b.play()