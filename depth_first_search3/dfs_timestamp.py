import sys
import math
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

sys.stdin = open('in.txt','r')
sys.stdout = open('out.txt', 'w')

WHITE = 0
GREY = 1
BLACK = 2

clock = 0
def dfsUtil(colour, parent, dist, ebunch, 
	discovery_time, completion_time, adj, u):
	global clock

	# GREY => STACKED 'u' (for processing)
	colour[u] = GREY
	discovery_time[u] = clock
	clock += 1

	# Processing node 'u' (printing)
	print(u, end=" ")

	# Exploring node 'v' (neighbour of node 'u') 
	# for IMMEDIATE processing 
	for v in adj[u]:

		# WHITE => NOT VISTED 
		if(colour[v]==WHITE):

			# Updating information of node 'v'
			parent[v] = u
			dist[v] = dist[u]+1

			# Adding edge u~v to DFS_tree
			ebunch.append((u,v))

			# Exploring node 'v' further
			dfsUtil(colour, parent, dist, ebunch, 
				discovery_time, completion_time, adj, v)

	# BLACK => COMPLETED processing of node 'u' (& all its children)
	colour[u] = BLACK 
	completion_time[u] = clock
	clock += 1


def depth_first_search(adj, n, source):
	# 'ebunch' is a list of edges obtained 
	# during traversal that form the DFS-Tree 
	ebunch = []

	'''
	lists to store primary and auxillary
	information during traversal process
	'''
	colour = [WHITE for i in range(n)]
	parent = [-1 for i in range(n)]
	dist = [math.inf for i in range(n)]
	discovery_time = [0 for i in range(n)]
	completion_time = [0 for i in range(n)]
	
	# Updating information of 'source'
	parent[source] = -1
	dist[source] = 0

	# Performing traversal (from source)
	dfsUtil(colour, parent, dist, ebunch, 
		discovery_time, completion_time, adj, source)
	
	# Completed traversal from 'source'	
	print()
	
	# Debugging 
	for i in range(n):		
		print(f"i={i}: colour[]={colour[i]},"\
		f" dist[]={dist[i]}, parent[]={parent[i]}"\
		f" start/end = {discovery_time[i]}/{completion_time[i]}")
	
	# returning tree obtained during DFS
	return (ebunch, discovery_time, completion_time)

def print_adj(adj):
	n = len(adj)
	for i in range(n):
		print(i, end=": ")
		for u in adj[i]:
			print(u, end=" ")
		print()

# n = number of nodes
# m = number of edges
n, m = map(int, input().split())

# Graph() Object from networkx library
G = nx.DiGraph()

# Adding 'n' nodes to Graph() Object 'G'
G.add_nodes_from([i for i in range(n)])

# Adjacency List to store 'n' vertex graph
adj = [[] for i in range(n)]

# Adding 'm' edges (to 'adj' and 'G')
for i in range(m):

	# u~v is an edge of the graph
	u, v = map(int, input().split())
	
	# Adding edge u~v to Adjaceny List,'adj'
	adj[u].append(v)

	# Adding edge u~v to Graph() Object, 'G'
	G.add_edge(u, v, color='silver', weight=2)

# Display Adjacency List  
print_adj(adj)

# Performing Depth First Search
tree, discovery_time, completion_time = depth_first_search(adj, n, 0)
print("Edges in DFS tree :", tree)

# Coloring different types of edges
for e in G.edges():
	u, v = e

	# back edge
	if(discovery_time[u] > discovery_time[v] and 
		completion_time[u] < completion_time[v]):
		G.add_edge(u, v, color='lightsalmon', weight=5)

	# cross edge
	if(discovery_time[u] > discovery_time[v] and 
		completion_time[u] > completion_time[v]):
		G.add_edge(u, v, color='lightblue', weight=5)

	# forward edge & tree edge
	if(discovery_time[u] < discovery_time[v] and 
		completion_time[u] > completion_time[v]):
		G.add_edge(u, v, color='lightgreen', weight=5)

# Coloring DFS tree edges (forward edges remain blue)
G.add_edges_from(tree, color='black', weight=5)

# color[] and width[] sent as parameter while drawing
colors = [G[u][v]['color'] for u,v in G.edges()]
weights = [G[u][v]['weight'] for u,v in G.edges()]

# time_stamps{} dictionary with key as nodes of graph
# value is string of format - "start_time/end_time"
# sent as parameter while drawing
time_stamps = {k:v for k,v in zip(G.nodes(),
	[f"\n\n\n{discovery_time[i]}/{completion_time[i]}" for i in range(n)])}

plt.plot()
pos = nx.circular_layout(G)
# refer to networkx docs for more drawing parameters
nx.draw_networkx(G, pos, with_labels=True, label='white')
nx.draw_networkx_edges(G, pos, edge_color=colors, width=weights,alpha=0.8)
nx.draw_networkx_nodes(G, pos, node_color='green', node_size=500)
nx.draw_networkx_labels(G, pos, labels=time_stamps,
	font_color='red',font_weight='bold' )

def make_proxy(clr, **kwargs):
    return Line2D([0,0],[0,0],color=clr, **kwargs)

# generate proxies with the above function
proxies = [make_proxy(clr, lw=5) for clr in 
['black', 'lightgreen', 'lightsalmon', 'lightblue']]
labels = ["TREE EDGE", "FORWARD EDGE", "BACK EDGE", "CROSS EDGE"]
plt.legend(proxies, labels)

plt.show()