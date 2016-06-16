import random
import os
import time
board=[]
posvec=[]
rows=25
cols=18
numx=50
check=False

for i in range(rows):
	templist=[]
	for j in range(cols):
		templist.append('.')
	board.append(templist)


for i in range(numx):
	while len(posvec)<numx:
		temppos=[random.randint(0,rows-1),random.randint(0,cols-1)]
		if temppos not in posvec:
			posvec.append(temppos)
print(posvec)

while check==False:
	for pos in posvec:
		board[pos[0]][pos[1]]='x'
	print()
	for list in board:
		for element in list:
			print(element, end=' ')
		print()
	check=True
	
	time.sleep(0.5)

	for pos in posvec:
		if pos[0]<rows-1 and board[pos[0]+1][pos[1]]!='x':				
			board[pos[0]][pos[1]]='.'
			pos[0]=pos[0]+1
			check=False
	os.system('cls')