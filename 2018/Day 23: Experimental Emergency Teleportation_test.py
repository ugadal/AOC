from random import randrange
from heapq import heappush, heappop
def calcd(x,y,bot):
	return abs(x-bot.x)+abs(y-bot.y)
class bot():
	def __init__(self,x,y,r):
		self.x=x
		self.y=y
		self.r=r
		self.ir=0
		self.hd=0
	def irof(self,allbots):
		v=0
		for b in allbots:
			if calcd(self,b)<=b.r:v+=1
		self.ir=v
	def __str__(self):
		return f"bot at {self.x},{self.y} radius {self.r}"
	# ~ def neighbors(self):
		# ~ N=[bot(self.x+dx,self.y+dy,self.z+dz,self.r) for dx,dy,dz in D]
		# ~ for n in N:n.hd=calcd(n,origin)
		# ~ return N
	def insquare(self,square):
		sx,sy,di=square
		tx,ty=sx+di-1,sy+di-1
		if sx<=self.x<=tx and sy<=self.y<=ty:return True
		if sx<=self.x+self.r<=tx and sy<=self.y<=ty:return True
		if sx<=self.x-self.r<=tx and sy<=self.y<=ty:return True
		if sx<=self.x<=tx and sy<=self.y+self.r<=ty:return True
		if sx<=self.x<=tx and sy<=self.y-self.r<=ty:return True
		return False
origin=bot(0,0,0)
Bots=[bot(randrange(5,95),randrange(5,95),randrange(1,35)) for x in range(8)]
for bot in Bots:print(bot)
rec=float("-inf")
proxd=-rec
for x in range(100):
	for y in range(100):
		ir=sum(1 if calcd(x,y,b)<=b.r else 0 for b in Bots)
		d=calcd(x,y,origin)
		if ir>rec:
			rec=ir
			proxd=calcd(x,y,origin)
			print(x,y,rec,d)
			fx=x
			fy=y
		if ir==rec:
			if d<proxd:
				proxd=d
				print("d-up",x,y,rec,d)
				fx=x
				fy=y
minx=miny=float("Inf")
maxx=maxy=float("-Inf")

for bot in Bots:
	minx=min(minx,bot.x)
	miny=min(miny,bot.y)
	maxx=max(maxx,bot.x)
	maxy=max(maxy,bot.y)
def overlap(square,bot):
	if bot.insquare(square):return True
	sx,sy,di=square
	if calcd(sx,sy,bot)<=bot.r:return True
	if calcd(sx+di-1,sy,bot)<=bot.r:return True
	if calcd(sx+di-1,sy+di-1,bot)<=bot.r:return True
	if calcd(sx,sy+di-1,bot)<=bot.r:return True
	return False
def splitsquare(square):
	sx,sy,di=square
	sz=di//2
	yield (sx,sy,sz)
	yield (sx+sz,sy,sz)
	yield (sx,sy+sz,sz)
	yield (sx+sz,sy+sz,sz)
print(minx,maxx)
print(miny,maxy)
square=(0,0,128)
over=sum(1 if overlap(square,bot) else 0 for bot in Bots)
print(square,over)
queue=[]
heappush(queue,(-over,square))
print(queue)
while queue:
	bir,square=heappop(queue)
	print(square)
	if square[2]==1:
		print(square)
		break
	for subsq in splitsquare(square):
		over=sum(1 if overlap(subsq,bot) else 0 for bot in Bots)
		if over:heappush(queue,(-over,subsq))
over=sum(1 if overlap((fx,fy,1),bot) else 0 for bot in Bots)
print("fx fy",fx,fy,over)
