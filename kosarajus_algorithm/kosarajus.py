def dfsUtil(G, visited, travel, s):
    if(visited[s]):
        return
    visited[s] = True
    for u in G[s]:
        if(not visited[u]):
            dfsUtil(G, visited, travel, u)
    travel.append(s)


def dfs(G, s=1):
    visited = {k: False for k in G.nodes}
    travel = []
    for u in G.nodes:
        if(not visited[u]):
            dfsUtil(G, visited, travel, u)
    return travel


def kosarajus(G):
    travel = reversed(dfs(G))
    H = G.reverse(copy=True)
    components = []
    visited = {k: False for k in G.nodes}
    for u in travel:
        if(not visited[u]):
            component = []
            dfsUtil(H, visited, component, u)
            components.append(component)
    return components
