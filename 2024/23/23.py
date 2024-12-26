import time
import re

with open('23.in') as f:
    dataset = f.readlines()
    graph = [line.rstrip('\n').split("-") for line in dataset]

# print(dataset)
cycles = []

#modified some code from https://stackoverflow.com/questions/12367801/finding-all-cycles-in-undirected-graphs 
#   
def findNewCycles(path):
    start_node = path[0]
    next_node= None
    sub = []
    if len(path) > 3:
        return

    #visit each edge and each node of each edge
    for edge in graph:
        node1, node2 = edge
        if start_node in edge:
            if node1 == start_node:
                next_node = node2
            else:
                next_node = node1
            if not visited(next_node, path):
                    # neighbor node not on path yet
                    sub = [next_node]
                    sub.extend(path)
                    # explore extended path
                    findNewCycles(sub)
            elif len(path) > 2  and next_node == path[-1]:
                    # cycle found
                    p = rotate_to_smallest(path)
                    inv = invert(p)
                    if isNew(p) and isNew(inv):
                        cycles.append(p)

def invert(path):
    return rotate_to_smallest(path[::-1])

#  rotate cycle path such that it begins with the smallest node
def rotate_to_smallest(path):
    n = path.index(min(path))
    return path[n:]+path[:n]

def isNew(path):
    return not path in cycles

def visited(node, path):
    return node in path

def part1():
    global graph
    global cycles
    for edge in graph:
        for node in edge:
            findNewCycles([node])
    count = 0
    for cy in cycles:
        path = [str(node) for node in cy]
        s = ",".join(path)
        if len(re.findall('t[a-z]',s)) > 0:
            print(s)
            count+=1
    return count

time1 = time.time()
print("Part 1",part1())
print(cycles)
time2 = time.time()


# working with code from: https://www.altcademy.com/blog/discover-the-largest-complete-subgraph/
def bron_kerbosch(graph, r=set(), p=None, x=set()):
    if p is None:
        p = set(graph.keys())

    if not p and not x:
        yield r
    else:
        u = next(iter(p | x))  # Choose a pivot vertex
        for v in p - graph[u]:
            yield from bron_kerbosch(graph, r | {v}, p & graph[v], x & graph[v])
            p.remove(v)
            x.add(v)

def find_largest_complete_subgraph(graph):
    cliques = list(bron_kerbosch(graph))
    return max(cliques, key=len)

newgraph = {}
def part2():
    for nodepair in graph:
        if nodepair[0] not in newgraph.keys():
            newgraph[nodepair[0]] = set()
        newgraph[nodepair[0]].add(nodepair[1])
        if nodepair[1] not in newgraph.keys():
            newgraph[nodepair[1]] = set()
        newgraph[nodepair[1]].add(nodepair[0])
    # for n in newgraph:
    #     print(n,newgraph[n])
    password = list(find_largest_complete_subgraph(newgraph))
    password.sort()
    return password

print("Part 2",",".join(part2()))
time3 = time.time()
print("Part 1 time:",time2-time1)
print("Part 2 time:",time3-time2)