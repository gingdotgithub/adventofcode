import networkx
import time

data = open('25.test').read().splitlines()
starttime = time.time()
g = networkx.Graph()

for line in data:
    node,neighbours = line.split(": ")
    neighbours = neighbours.split(" ")
    #print(neighbours)
    for n in neighbours:
        #print('adding',node,n)
        g.add_edge(node,n)
        #g.add_edge(n,node)

print(g)
g.remove_edges_from(networkx.minimum_edge_cut(g))
print(g)
a,b = networkx.connected_components(g)
print(a,b)
endtime = time.time()
print("part 1:",len(a)*len(b))
print("part 1 timing:",endtime-starttime)
#once you learn about networkx and graphs, then this one is a bit of a cheat-easy