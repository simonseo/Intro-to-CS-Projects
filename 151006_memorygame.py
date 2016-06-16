import random
import os
import time
row=5
col=8
turn=1
playernum=2
highScore=0
board=[]
card=[]
score=[]
winner=[]
victory=False
targetString1,targetString2,target1,target2='','','',''

def printboard(target1,target2):
	print('\n ',end='|')
	for i in range(col):
		print(i,end='|')
	print()
	for i in range(row):
		print(i,end='|')
		for j in range(col):
			if target1==['where']:
				print (board[i][j][2],end='|')
			elif [i,j]==target1 or [i,j]==target2:
				print (board[i][j][2],end='|')	
			else:
				print (board[i][j][board[i][j][3]],end='|')
		print()

#CARDLIST
for i in range(row*col//2):
	card.append(chr(i+65))
	card.append(chr(i+65))
random.shuffle(card)

#BUILD A BOARD THAT FLIPS or I could make a hiddenboard and a displayboard
for i in range(row):
	templist=[]
	for j in range(col):
		templist.append(['-',' ',card[i*col+j],False])	
	board.append(templist)

#SCORECARD
for i in range(playernum):
	score.append(0)


while not victory:
	player=(turn+1)%playernum+1
	
	os.system('cls')

	printboard([-1,-1],[-1,-1])

	#errorchecking code + INPUT TARGET here
	targetString1=input('player #'+str(player)+': input target1 (Ex. 22): ')
	if targetString1=='where': 
		printboard(['where'],[])
		time.sleep(3)
		continue
	while len(targetString1)!=2 or not targetString1.isdigit() or not(0<=int(targetString1[0])<=row-1 and 0<=int(targetString1[1])<=col-1) or board[int(targetString1[0])][int(targetString1[1])][3]==True:
		targetString1=input('Error. player #'+str(player)+': input target1 (Ex. 22): ')
	target1=[int(targetString1[0]),int(targetString1[1])]

	targetString2=input('player #'+str(player)+': input target2 (Ex. 32): ')
	while len(targetString2)!=2 or not targetString2.isdigit() or not(0<=int(targetString2[0])<=row-1 and 0<=int(targetString2[1])<=col-1) or board[int(targetString2[0])][int(targetString2[1])][3]==True:
		targetString2=input('Error. player #'+str(player)+': input target2 (Ex. 32): ')
	target2=[int(targetString2[0]),int(targetString2[1])]
	printboard(target1,target2)

	time.sleep(2)

	if board[target1[0]][target1[1]][2]==board[target2[0]][target2[1]][2]:
		board[target1[0]][target1[1]][3]=True
		board[target2[0]][target2[1]][3]=True
		score[player-1]+=1

		#VICTORY CHECK
		victory=True
		for i in range(row):
			for j in range(col):
				if board[i][j][3]==False:
					victory=False
		if victory==False:
			continue
	
	turn+=1



for player in range(playernum):
	if highScore<score[player]:
		highScore=score[player]
		winner=[]
		winner.append(player+1)
	elif highScore==score[player]:
		winner.append(player+1)

if len(winner)==1:
	print('The winner is player #',winner[0])
else:
	print('The winners are:',winner)