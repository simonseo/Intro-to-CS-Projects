import random

class MineTile:
	def __init__(self,row,col,val):
		self.row=row
		self.col=col
		self.val=val
		#'' '1' '2' ... '8' 'M'
		self.hidden=True

	def isMine(self):
		if self.val=='M':
			return True
		else:
			return False

class Board:

	def __init__(self,numRows,numCols,numMines):
		self.numRows=numRows
		self.numCols=numCols
		self.numMines=numMines
		self.numUnopened=numRows*numCols
		self.neighborList=[(-1,-1),(-1,0),(-1,+1),(0,-1),(0,1),(+1,-1),(+1,0),(+1,+1)]
		self.board=[]
		
		for r in range(self.numRows):
			for c in range(self.numCols):
				self.board.append(MineTile(r,c,' '))
		self.assignRandMines(numMines)

		for r in range(self.numRows):
			for c in range(self.numCols):
				if not self.getTile(r,c).isMine():
					self.getTile(r,c).val=self.countMine(r,c)
		

	def assignRandMines(self,numMines):
		randlist=[]
		mineCount=0
		while mineCount<numMines:
			randPos=[random.randint(0,self.numRows-1),random.randint(0,self.numCols-1)]
			if not randPos in randlist:
				randlist.append(randPos)
				mineCount+=1

		for minePos in randlist:
			self.getTile(minePos[0],minePos[1]).val='M'


	def displayBoard(self):
		print(' ',end='|')
		for c in range(self.numCols):
			print(c,end='|')
		print()
		for r in range(self.numRows):
			print(r,end='|')
			for c in range(self.numCols):
				if self.getTile(r,c).hidden:
					print(' ', end='|')
				elif self.getTile(r,c).val==0:
					print('.', end='|')
				else:
					print(self.getTile(r,c).val,end='|')
			print()

	def getTile(self,row,col):
		for tile in self.board:
			if tile.row==row and tile.col==col:
				return tile

	def countMine(self,row,col):
		count=0
		for neighbor in self.neighborList:
			if 0<=row+neighbor[0]<=self.numRows-1 and 0<=col+neighbor[1]<=self.numCols-1 and self.getTile(row+neighbor[0],col+neighbor[1]).isMine():
				count+=1
		return count
		

	def userHit(self,row,col):
		if not self.getTile(row,col).hidden:
			print('already hit!')
			self.userHit(int(input('row: ')),int(input('col: ')))

		print("The tile is a mine? ", self.getTile(row,col).isMine())
		if self.getTile(row,col).isMine():
			print('game over')
		else:
			self.openSpaces(row,col)
			print()
			self.displayBoard()
			if self.numUnopened==self.numMines:
				print('game over')
				return
			self.userHit(int(input('row: ')),int(input('col: ')))

	def openSpaces(self,row,col):
		self.getTile(row,col).hidden=False
		self.numUnopened-=1
		if self.getTile(row,col).val==0:
			for neighbor in self.neighborList:
				if 0<=row+neighbor[0]<=self.numRows-1 and 0<=col+neighbor[1]<=self.numCols-1:
					if self.getTile(row+neighbor[0],col+neighbor[1]).val!='M':
						if self.getTile(row+neighbor[0],col+neighbor[1]).hidden:
							self.openSpaces(row+neighbor[0],col+neighbor[1])

b1=Board(10,10,10)
b1.displayBoard()
b1.userHit(int(input('row: ')),int(input('col: ')))

