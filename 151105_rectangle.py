class Point:	
	"""	Point	class	represents	and	manipulates	x,y coords.	"""	
	def __init__(self,x=0,y=0):	
		"""	creates	a	point	with	(x,y),	default	is	at	origin	(0,0)	"""	
		self.x=x	
		self.y=y	
	def distanceFromOrigin (self):	
		"""	computes	the	distance	between	the	point	and	the	origin	(0,0)"""	
		return((self.x**2)+(self.y**2))**0.5	
	def __str__(self):	
		return"({0},{1})".format(self.x,self.y)
	def halfway (self,target):
		mx=(self.x+target.x)/2
		my=(self.y+target.y)/2
		return Point(mx,my)

class Rectangle:
	def __init__(self, lowerLeftPoint, width, height):
		self.lowerLeftPoint=lowerLeftPoint
		self.width=width
		self.height=height
	def __str__(self):
		return "(({0},{1}),{2},{3})".format(self.lowerLeftPoint.x,self.lowerLeftPoint.y,self.width,self.height)
	def grow(self,deltaX,deltaY):
		self.width = self.width + deltaX
		self.height = self.height + deltaY
	def move(self, deltaX, deltaY):
		self.lowerLeftPoint = Point(self.lowerLeftPoint.x + deltaX,self.lowerLeftPoint.y+deltaY)

r1=Rectangle(Point(10,5),100,50)	
print(r1)
r1.grow(25,-10)
print(r1)
r1.move(-10,10)
print(r1)
