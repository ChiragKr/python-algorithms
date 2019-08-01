import sys
import math
import networkx as nx
import matplotlib.pyplot as plt

sys.stdin = open('in.txt','r')
sys.stdout = open('out.txt', 'w')

WHITE = 0
GREY = 1
BLACK = 2

def dfsUtil(colour, parent, dist, ebunch, adj, u):
	# GREY => STACKED 'u' (for processing)
	colour[u] = GREY

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
			dfsUtil(colour, parent, dist, ebunch, adj, v)

	# BLACK => COMPLETED processing of node 'u' (& all its children)
	colour[u] = BLACK

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
	
	# Updating information of 'source'
	parent[source] = -1
	dist[source] = 0

	# Performing traversal (from source)
	dfsUtil(colour, parent, dist, ebunch, adj, source)
	
	# Completed traversal from 'source'	
	print()
	
	# Debugging 
	for i in range(n):
		if(i==source):
			continue		
		print(f"i={i}: colour[]={colour[i]},"\
		f" dist[]={dist[i]}, parent[]={parent[i]}")
	
	# returning tree obtained during DFS
	return ebunch

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
G = nx.Graph()

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
	adj[v].append(u)

	# Adding edge u~v to Graph() Object, 'G'
	G.add_edge(u, v, color='blue', weight=2)

# Display Adjacency List  
print_adj(adj)

ebunch = depth_first_search(adj, n, 0)
print("Edges in DFS tree :", ebunch)

''' 
Drawing 'G' using networkx 'draw_...' fucntions
'''

# Coloring DFS-Tree edges red
G.add_edges_from(ebunch, color='red', weight=8)
# color[] and width[] sent as parameter while drawring
colors = [G[u][v]['color'] for u,v in G.edges()]
weights = [G[u][v]['weight'] for u,v in G.edges()]


plt.plot()
pos = nx.spring_layout(G)
# refer to networkx docs for more drawing parameters
nx.draw_networkx(G, pos, with_labels=True)
nx.draw_networkx_edges(G, pos, edge_color=colors, width=weights)
nx.draw_networkx_nodes(G, pos, node_color='black', node_size=300)
nx.draw_networkx_labels(G, pos, font_color='white',font_weight='bold' )
plt.show()