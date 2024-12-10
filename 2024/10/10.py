with open('10.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]


zeros = []
h = len(dataset)
w = len(dataset[0])
print(w,h)


def dfs(visited,x,y):
    if (x,y) not in visited:
        visited.add((x,y))
        for neighbour in getneighbours(x,y):
            if dataset[neighbour[1]][neighbour[0]] != '.':
                if int(dataset[neighbour[1]][neighbour[0]]) - int(dataset[y][x]) == 1:
                    if dataset[neighbour[1]][neighbour[0]] == '9':
                        print('found one',neighbour[0],neighbour[1])
                        if [neighbour[0],neighbour[1]] not in trailends:
                            print("and its new!")
                            trailends.append([neighbour[0],neighbour[1]])
                    else:
                        dfs(visited,neighbour[0],neighbour[1])

def getneighbours(x,y):
    neighbours = [[x,y-1],[x+1,y],[x,y+1],[x-1,y]]
    goodneighbours = []
    for coord in neighbours:
        if coord[0] >= 0 and coord[1] >= 0 and coord[0] < w and coord[1] < h:
            goodneighbours.append(coord)
    return goodneighbours

visited = set()
trailends = []
score = 0
for y in range(h):
    for x in range(w):
        if dataset[y][x] == '0':
            trailends = []
            visited = set()
            zeros.append([x,y])
            print("doing",x,y)
            dfs(visited,x,y)
            score += len(trailends)
print(zeros)
print("part 1",score)

