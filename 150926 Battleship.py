###Let's Play the game of Battleship-SET CONSTANTS
import random
ship_health=4
shots = 0
board=[]
count=0
while count < 10:
      yValue=[]
      yValue.append(count)
      for j in range(10): yValue.append('□')
      board.append(yValue)
      count=count+1
###SET SHIP POSITION azim[(x XOR y),(-1 XOR +1)]
azim=[random.randint(0,1),2*random.randint(0,1)-1]
ship_len_4=[[random.randint(0,9),random.randint(0,9)],[0,0],[0,0],[0,0]]
for i in range(1,4):
      if 1 <= ship_len_4[i-1][azim[0]]+azim[1] <=10:
            ship_len_4[i][azim[0]]=ship_len_4[i-1][azim[0]]+azim[1]
            ship_len_4[i][abs(azim[0]-1)]=ship_len_4[i-1][abs(azim[0]-1)]
      else:
            azim=[azim[0],azim[1]*(-1)]
            ship_len_4[i][azim[0]]=ship_len_4[i-1][azim[0]]+(azim[1]*i)
            ship_len_4[i][abs(azim[0]-1)]=ship_len_4[i-1][abs(azim[0]-1)]            
###PLAY UNTIL SHIP SINKS
while True:
      print('\nshots:',shots,'\n |A|B|C|D|E|F|G|H|I|J|',sep='')
      for rows in board:
            for i in rows:
                  if str(i).isdigit(): print(i, end='|')
                  elif i==True: print('■', end='|')
                  elif i==False: print(' ', end='|')
                  else: print(i, end='|')
            print()
      if ship_health==0: break
      targetString=input('input target (Ex. A1): ')
      if targetString=='where':
            for i in range(4):
                  print()
                  print(chr(ship_len_4[i][0]+96).upper(),ship_len_4[i][1],sep='',end=' ')
      elif targetString=='end':
            break
      elif len(targetString) !=2 or not(targetString[0].isalpha() and targetString[1].isdigit()):
            print('syntax error. input again.')
            continue
      else:
            target=[ord(targetString[0].lower())-96,int(targetString[1])]
            print(target)
            if 0<=target[1]<=9 and 1<=target[0]<=10:
                  if board[target[1]][target[0]] == '□':
                        shots+=1
                        if target in ship_len_4:
                              board[target[1]][target[0]] = True
                              ship_health -=1
                              print('Hit!')
                        else:
                              board[target[1]][target[0]] = False
                              print('Try again!')
                  else: print('already hit!')
###GAMEOVER                  
print('\nshots:',shots,'\nGAME OVER. CONGRATULATIONS',sep=' ')
