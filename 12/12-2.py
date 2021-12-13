mygraph = {}
paths = []

def gfind(graph, currentVertex, path, visited, freepass = False):
    path.append(currentVertex)
    if freepass:
        visited.remove('freepass')
    if currentVertex.islower() and freepass != True:
        visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        usingfreepass = False
        if vertex in visited and vertex != 'start' and vertex != 'end' and 'freepass' in visited:
            usingfreepass = True
        if vertex not in visited or usingfreepass:
            gfind(graph, vertex, path.copy(), visited.copy(), usingfreepass)
    if currentVertex == 'end':
        paths.append(path)

while True:
    readline = input()
    if readline == '':
        break
    edge = readline.split('-')
    if edge[0] not in mygraph.keys():
        mygraph[edge[0]] = [edge[1]]
    else:
        mygraph[edge[0]].append(edge[1])
    if edge[1] not in mygraph.keys():
        mygraph[edge[1]] = [edge[0]]
    else:
        mygraph[edge[1]].append(edge[0])

print(mygraph)
gfind(mygraph, 'start', [], ['freepass'])
for path in sorted(paths):
    print(path)
print(len(paths))