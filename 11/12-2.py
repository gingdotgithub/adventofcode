mygraph = {}
paths = []

def gfind(graph, currentVertex, visited):
    if currentVertex.islower():
        visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            gfind(graph, vertex, visited.copy())
    if currentVertex == 'end':
        paths.append(visited)

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
gfind(mygraph, 'start', [])
print(paths)
print(len(paths))