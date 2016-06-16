import time, os
from alphabets import alphabets
screenWidth=20
message='SIMON'
messagelen=len(message)


shift=20
repeat=0
while repeat<200:
	print(repeat)
	for i in range(5):
		print(shift*' ',end='')
		for letterIndex in range(max(0,int((messagelen*7-shift)/7)),messagelen):
			#if letterIndex==int((len(message)*6-shift)/6):
			if shift<0:
				print(alphabets[message[letterIndex]][i][(len(message)*7-shift)%7:],end=' ')
			else:
				print(alphabets[message[letterIndex]][i],end=' ')
			print(' ',end='')
		print()
	print()

	shift-=1
	if shift<-messagelen*6:
		shift=20
	repeat+=1
