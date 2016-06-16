import os
import time
row=6
col=7
board=[]
checker=[' ','○','●','☆','★']
turn=1
full=False
winner='no one'

def printboard():
	print()
	for i in range(col):
		print(i+1,end='|')
	print()
	for j in range(row):
		for i in range(col):
			print(board[i][j],end='|')
		print()

for i in range(col):
	templist=[]
	for j in range(row):
		templist.append(checker[0])
	board.append(templist)

while(winner=='no one'):
	player=(turn+1)%2+1
	printboard()

	targetString=input('Player '+str(player)+', input column value (Ex. 3): ')
	while len(targetString)!=1 or not(targetString.isdigit()) or not(1<=int(float(targetString))<=col+1) or not(checker[0] in board[int(float(targetString))-1]):
		targetString=input('Input Error. Player '+str(player)+', input column value (Ex. 3): ')
	targetcol=int(float(targetString))-1
 	 
	board[targetcol][0]=checker[player]
	
	targetrow=0
	for i in range(row-1):
		if board[targetcol][i+1]==checker[0]:
			board[targetcol][i]=checker[0]
			board[targetcol][i+1]=checker[player]
			targetrow=i+1
	
	#check column
	victory=True
	if targetrow>row-4:
		victory=False
	else:
		for i in range(3):
			if board[targetcol][targetrow+i]!=board[targetcol][targetrow+i+1]:
				victory=False
	if victory:
		winner=player
		for i in range(4):
			board[targetcol][targetrow+i]=checker[player+2]


	#check row
	count=0
	for i in range(col-1):
		if board[i][targetrow]==board[i+1][targetrow]:
			count+=1
			end=i+1
		if count==3:
			winner=player
			for i in range(end-3,end+1):
				board[i][targetrow]=checker[player+2]
			break
		elif board[i+1][targetrow]!=checker[player]:
			count=0


	
	#check diagonal
	count1=0
	count2=0

	#negative slope
	i=0
	end1=targetcol
	end2=targetrow
	while targetrow-i-1>=0 and targetcol-i-1>=0 and count1!=3 and i<3 and board[targetcol-i][targetrow-i]==checker[player]:
		if board[targetcol-i][targetrow-i]==board[targetcol-i-1][targetrow-i-1]:
			count1+=1
		i+=1
	i=0
	while targetrow+i+1<=row-1 and targetcol+i+1<=col-1 and count1!=3 and i<3 and board[targetcol+i][targetrow+i]==checker[player]:
		if board[targetcol+i][targetrow+i]==board[targetcol+i+1][targetrow+i+1]:
			count1+=1
			end1=targetcol+i+1
			end2=targetrow+i+1
		i+=1
	if count1==3: 
		winner=player
		for i in range(4):
			board[end1-i][end2-i]=checker[player+2]

	#positive slope
	i=0
	end1=targetcol
	end2=targetrow
	while targetrow+i+1<=row-1 and targetcol-i-1>=0 and count2!=3 and i<3 and board[targetcol-i][targetrow+i]==checker[player]:
		if board[targetcol-i][targetrow+i]==board[targetcol-i-1][targetrow+i+1]:
			count2+=1
		i+=1
	i=0
	while targetrow-i-1>=0 and targetcol+i+1<=col-1 and count2!=3 and i<3 and board[targetcol+i][targetrow-i]==checker[player]:
		if board[targetcol+i][targetrow-i]==board[targetcol+i+1][targetrow-i-1]:
			count2+=1
			end1=targetcol+i+1
			end2=targetrow-i-1
		i+=1
	
	if count2==3:
		winner=player
		for i in range(4):
			board[end1-i][end2+i]=checker[player+2]
	

	#CHECK FULL
	full=True
	for i in range(col):
		if board[i][0]==checker[0]:
			full=False
	if full:
		print('full')
		break

	turn+=1
printboard()
print('Player #',winner,'wins')
time.sleep(4)