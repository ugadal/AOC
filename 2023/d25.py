import itertools as it
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
exp="""jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""
def full():
		vec=[True]+[False for _ in LV[1:]]
		before=[v for v in vec]
		while True:
			# ~ print(vec)
			nvec=[any([s and ((a,b) in edges) for s,a in zip(vec,LV)]) for b in LV]
			# ~ print(nvec)
			after=[a or b for a,b in zip(before,nvec)]
			# ~ print("merged",after)
			# ~ new=[not a and b for a,b in]
			if all(after):return 
			if after==vec:
				print (a,b,c,f"subgraphed {vec.count(True)} {vec.count(False)}")
				return
			vec=[v for v in after]
edges=set()
simpleedges=set()

V=set()
cut="htj,pcc  dlk,pjj  bbg,htb"
# ~ for line in exp.splitlines():
for line in open("d25.txt").read().splitlines():
	l,r=line.split(": ")
	V.add(l)
	for s in r.split():
		edges.add((l,s))
		edges.add((s,l))
		simpleedges.add((s,l))
		V.add(s)
		G.add_edge(s,l,name=(s,l))
# ~ pos = nx.spring_layout(G)

# ~ nx.draw(
    # ~ G, pos, edge_color='black', width=1, linewidths=1,
    # ~ node_size=500, node_color='pink', alpha=0.9,
    # ~ labels={node: node for node in G.nodes()}
# ~ )
# ~ nx.draw(G)
# ~ nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G))
# ~ nx.draw_networkx_edges(G, pos=nx.spring_layout(G))
# ~ plt.show()
# ~ input()
LV=list(V)
LE=list(simpleedges)
LV.sort()
edges.remove(("htj","pcc"))
edges.remove(("pcc","htj"))
edges.remove(("dlk","pjj"))
edges.remove(("pjj","dlk"))
edges.remove(("bbg","htb"))
a=b=c=""
print(full())
exit()
for a,b,c in it.combinations(LE,3):
	# ~ print(a,b,c)
	for l,r in (a,b,c):
		edges.remove((l,r))
		edges.remove((r,l))
	full()
	for l,r in (a,b,c):
		edges.add((l,r))
		edges.add((r,l))
