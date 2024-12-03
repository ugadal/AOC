#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import itertools as it
from collections import deque
# ~ from tqdm import tqdm
day=sys.argv[0].split(".")[0][1:]
print(day)
"""geode needs 2 ore and 8 obs > obs robot <=8
							  orebot <=2
obs_bot needs 4 ore and 8 clay >orebot <=4
								claybot<=8
clay bots needs 3 ore		orebot <=3
ore bot needs 4 ore 		orebot<=4

M_obs_bot=max(orn_orbot,orn_obsbot,orn_geobot)
M_clay_bots=cln_obsbot
M_ore_bot=max(orn_orbot,
"""


import re
exp=f"exp{day}.txt"
real=f"d{day}.txt"
s=re.compile(r"^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.")
BP={}
class bp():
	def __init__(self,bpid,orn_orbot,orn_clbot,orn_obsbot,cln_obsbot,orn_geobot,obsn_geobot):
		self.bpid=bpid
		self.orn_orbot=orn_orbot
		self.orn_clbot=orn_clbot
		
		self.orn_obsbot=orn_obsbot
		self.cln_obsbot=cln_obsbot
		
		self.orn_geobot=orn_geobot
		self.obsn_geobot=obsn_geobot
		self.Mobs_bot=obsn_geobot
		self.Mcl_bot=cln_obsbot
		self.Morbot=max(orn_orbot,orn_clbot,orn_obsbot,orn_geobot)
		BP[self.bpid]=self
lines=open(exp).read().strip().splitlines()
lines=open(real).read().strip().splitlines()
for line in lines:bp(*map(int,s.match(line).groups()))
# ~ print(BP)
# ~ exit()
tl=32
seen={}
def dfs(time,bp,orebot=1,claybot=0,obsbot=0,geobot=0,ore=0,clay=0,obs=0,geod=0):
	# ~ print(f"recur: {time} orebot:{orebot} claybot:{claybot} obsbot:{obsbot} geobot:{geobot} ore:{ore} clay:{clay} obs:{obs} geodes: {geod}")
	hc=hash((time,orebot,claybot,obsbot,geobot,ore,clay,obs,geod))
	if hc in seen:return seen[hc]
	mv=0
	if time>tl:return geod
	mv=max(mv,dfs(time+1,bp,orebot,claybot,obsbot,geobot,ore+orebot,clay+claybot,obs+obsbot,geod+geobot))
	if ore>=bp.orn_orbot and orebot<bp.Morbot:
		mv=max(mv,dfs(time+1,bp,orebot+1,claybot,obsbot,geobot, ore+orebot-bp.orn_orbot ,clay+claybot,obs+obsbot,geod+geobot))
	if ore>=bp.orn_clbot and claybot<bp.Mcl_bot:
		mv=max(mv,dfs(time+1,bp,orebot,claybot+1,obsbot,geobot, ore+orebot-bp.orn_clbot ,clay+claybot,obs+obsbot,geod+geobot))
	if ore>=bp.orn_obsbot and clay>=bp.cln_obsbot and obsbot<bp.Mobs_bot:
		mv=max(mv,dfs(time+1,bp,orebot,claybot,obsbot+1,geobot, ore+orebot-bp.orn_obsbot ,clay+claybot-bp.cln_obsbot,obs+obsbot,geod+geobot))
	if ore>=bp.orn_geobot and obs>=bp.obsn_geobot:
		mv=max(mv,dfs(time+1,bp,orebot,claybot,obsbot,geobot+1, ore+orebot-bp.orn_geobot ,clay+claybot,obs+obsbot-bp.obsn_geobot,geod+geobot))
	
	seen[hc]=mv
	return mv
ttl=1
for k in [1,2,3]:
	seen={}
	for t in range(tl+1,0,-1):
		v=dfs(t,BP[k])
		print(t,v)
	ttl*=v
print (ttl)
