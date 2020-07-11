import sys
import networkx as nx
from kosarajus import kosarajus
from plot import plot


def main(argc, argv):
    '''
    DESCRIPTION :
    Client code using other (imported) modules.

    ARGUMENTS :
    argv : [''] arguments passed in command line
    argc : (int) # of arguments passed (=len(argv))

    RETURNS :
    0 on successful execution. Non-zero otherwise.
    '''
    # VALIDATE INPUTS

    # I/O FILES (if needed)
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    # WRITE CODE HERE
    n, m = map(int, input().split())
    # print(f"n = {n}, m = {m}")
    G = nx.DiGraph()
    G.add_nodes_from(range(1, n+1))
    # print(G.nodes)
    for _ in range(m):
        src, dst = map(int, input().split())
        G.add_edge(src, dst)
    components = kosarajus(G)
    print(components)
    plot(G, components)
    return 0


if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    if(main(argc, argv) == 0):
        print(argv[0]+" execution: SUCCESS")
    else:
        print(argv[0]+" execution: FAILURE")

# input.txt
# 7 10
# 1 2
# 1 4
# 2 1
# 2 5
# 3 2
# 3 7
# 5 4
# 6 5
# 6 3
# 7 6
#
