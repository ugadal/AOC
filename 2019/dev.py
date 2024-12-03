#!/usr/bin/env python3
#
#  dev.py
#  
class test():
	def __init__(self):
		self.Q=[]
		self.flow=self.run()
	def run(self):
		print("started",self.Q)
		# ~ for x in range(5):
			# ~ yield x
		yield "Done"
		return

x=test()
v=next(x.flow)
print(v)
exit()
for v in x.flow:
	print(v)
