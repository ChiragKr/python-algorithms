import networkx as nx
import matplotlib.pyplot as plt


def plot(G, components):
    # plotting
    node_group = [-1 for _ in G.nodes]
    for group_ID, component in enumerate(components):
        for u in component:
            node_group[u-1] = group_ID
    # print(node_group)
    plt.plot()
    pos = nx.spring_layout(G)
    # refer to networkx docs for more drawing parameters
    nx.draw_networkx(G, pos, with_labels=True, connectionstyle="arc3,rad=0.1")
    nx.draw_networkx_nodes(G, pos, node_color=node_group,
                           cmap=plt.cm.Set1, node_size=300)
    # nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20, width=3, alpha=1)
    plt.show()
