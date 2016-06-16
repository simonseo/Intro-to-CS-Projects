import os
import time
board=[]
playernum=2
playerlist=['No one']
for i in range(playernum):
	playerlist.append(input('add player name: '))
checker=['.','X','O','@','#']
square=3
full=False
winner=playerlist[0]

for i in range(square):
	templist=[]
	for j in range(square):
		templist.append('.')
	board.append(templist)

turn=0
while(winner==playerlist[0]):
	player=turn%playernum+1
	print(' |',end='')
	for i in range(square):
		print(i,end='|')
	print()
	for i in range(square):
		print(i,end='|')
		for element in board[i]:
			print(element,end=' ')
		print()

	where=input('input coordinate, player'+str(playerlist[player])+' Ex. 1,0 ')
	if not(len(where) ==3 and where[0].isdigit() and where[2].isdigit() and 0<=int(where[0])<=square-1 and 0<=int(where[2])<=square-1):
		print('syntax error. input again.')
		continue
	else:
		where=[int(where[0]),int(where[2])]
		if board[where[0]][where[1]]==checker[0]:
			turn+=1
			board[where[0]][where[1]]=checker[player]
		else: 
			print('put it somewhere else!')
			continue
	

	for i in range(square):
		count1=0
		count2=0
		for j in range(square-1):
			if board[i][j]==board[i][j+1] and board[i][j]!=checker[0]:
				count1+=1
			if board[j][i]==board[j+1][i] and board[j][i]!=checker[0]:
				count2+=1
			print(count1, count2)
		if count1==square-1 or count2==square-1: 
			winner=playerlist[player]
			print(winner)
			break


	count1=0
	count2=0
	for i in range(square-1):
		for j in range(square-1):
			if board[i][j]==board[i+1][j+1] and board[i][j]!=checker[0]:
				count1+=1
			if board[i][square-1-j]==board[i+1][square-2-j] and board[square-1-j][i]!=checker[0]:
				count2+=1
			print(count1, count2)

	if count1==square-1 or count2==square-1: 
		winner=playerlist[player]
		print(winner)
		break

	full=True
	for i in range(square):
		for j in range(square):
			if checker[0] == board[i][j]:
				full=False
	if full: 
		print(winner)
		break
	
