#!/usr/bin/env python3
#
# ~ from functools import cache
import pyyed as nx
G=nx.Graph()
import matplotlib.pyplot as plt
sep="\n\n"
Known=set()
fn,part="d24.txt",0
# ~ x07 AND y07 -> ncs
# ~ y24 AND x24 -> wrf
# ~ x19 XOR y19 -> tsm
# ~ x40 XOR y40 -> svt
# ~ G.add_nodes_from(["x07","AND","y07","ncs"])
# ~ G.add_edge("x07","AND")
# ~ G.add_edge("y07","AND")
# ~ G.add_edge("AND","ncs")
# ~ G.add_nodes_from(["y24","AND","x24","wrf"])
# ~ G.add_edge("y24","AND")
# ~ G.add_edge("x24","AND")
# ~ G.add_edge("AND","wrf")
# ~ nx.draw(G,with_labels=True)
# ~ plt.show()
# ~ exit()
K,T=open(fn).read().split(sep)
for opn,cl in enumerate(T.splitlines()):
	a,op,b,unused,target=cl.split()
	if not a in Known:
		G.add_node(a,shape="roundrectangle",shape_fill="#A00000")
		Known.add(a)
	if not b in Known:
		G.add_node(b,shape="roundrectangle",shape_fill="#A00000")
		Known.add(b)
	if not target in Known:
		G.add_node(target,shape="roundrectangle",shape_fill="#00A000")
		Known.add(target)
	opno=op+str(opn)
	match op:
		case "XOR":sh="triangle"
		case "OR":sh="ellipse"
		case "AND":sh="diamond"
	G.add_node(opno,shape=sh)
	G.add_edge(a,opno)
	G.add_edge(b,opno)
	G.add_edge(opno,target)
G.write_graph('d24.graphml')
exit()
nx.draw(G,with_labels=True)
plt.show()
Known={}
for l in K.splitlines():
	k,v=l.split(": ")
	Known[k]=True if int(v) else False
# ~ print(Known)
todo= T.splitlines()
while todo:
	cl=todo.pop(0)
	a,op,b,unused,target=cl.split()
	# ~ print(len(todo),a,op,b,target)
	if not (a in Known and b in Known):
		# ~ print(a,a in Known,b,b in Known,"skipping")
		todo.append(cl)
		continue
	# ~ print(a,a in Known,b,b in Known,"going on")
	a=Known[a]
	b=Known[b]
	# ~ print(a,op,b)
	# ~ input()
	match op:
		case 'OR':
			Known[target]=a or b
		case 'AND':
			Known[target]=a and b
		case 'XOR':
			Known[target]=a ^ b
nz=[k for k in Known.keys() if k.startswith("z") ]
nz.sort()
nz.reverse()
print(nz)
bs="".join(["1" if Known[k] else "0" for k in nz])
print(int(bs,2))
