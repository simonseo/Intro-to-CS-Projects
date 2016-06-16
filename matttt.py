import matplotlib.pyplot as plt
import math

'''theta=0
increment=0.24
x=[]
y=[]

for r in range(200):
	theta+=increment
	if r%10==0: increment-=0.01
	x.append(r*math.cos(math.pi*theta))
	y.append(r*math.sin(math.pi*theta))

plt.plot(x,y)
plt.show()'''

def square(a):
	return(a**2)

x=list(range(-100,100))
y=list(map(square,x))

plt.plot(x,y)
plt.show()

