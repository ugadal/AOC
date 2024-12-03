#!/usr/bin/env python3
#
#  mylib.py
#  
#  Copyright 2023 dcoorna@gmail.com
#  Coornaert David PhD
#  
#  


import sys
from functools import wraps

def myint(s):
	r=1
	if s.startswith("-"):
		r=-1
		s=s[1:]
	if s.isdigit():return r*int(s)
	return D.get(s,0)


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

class manager():
	def __init__(self,thisconst):
		self.data={}
		self.con=thisconst
	def gen(self,key):
		if self.con==list:return []
		if self.con==dict:return {}
		if self.con==set:return set()
		return self.con(key)
	def get(self,key):
		if key in self.data:return self.data[key]
		no=self.gen(key)
		self.data[key]=no
		return no
# ~ def flip(L):return tuple(row[::-1] for row in L)
# ~ def trans(L):return tuple(zip(*L))
def flip(L):
	if type(L)==list:return L[::-1]
	if type(L)==tuple:return tuple(row[::-1] for row in L)
def mirror(L):return [l[::-1] for l in L]
def transpose(G):
	if type(G)==list:return list(map(list,zip(*G)))
	if type(G)==tuple:return tuple(zip(*L))

# ~ rotate right
# ~ x,y=y,-x
# ~ 
# ~ rotate leftt
# ~ x,y=-y,x

def main(args):
    return 0		

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
