import time

time1=time.time()
with open('10.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
time2=time.time()

zeros = []
h = len(dataset)
w = len(dataset[0])
# print(w,h)


def dfs(x,y):
    for neighbour in getneighbours(x,y):
        if dataset[neighbour[1]][neighbour[0]] != '.':
            if int(dataset[neighbour[1]][neighbour[0]]) - int(dataset[y][x]) == 1:
                if dataset[neighbour[1]][neighbour[0]] == '9':
                    if [neighbour[0],neighbour[1]] not in trailends:
                        trailends.append([neighbour[0],neighbour[1]])
                else:
                    dfs(neighbour[0],neighbour[1])

def getneighbours(x,y):
    neighbours = [[x,y-1],[x+1,y],[x,y+1],[x-1,y]]
    goodneighbours = []
    for coord in neighbours:
        if coord[0] >= 0 and coord[1] >= 0 and coord[0] < w and coord[1] < h:
            goodneighbours.append(coord)
    return goodneighbours

trailends = []
score = 0
for y in range(h):
    for x in range(w):
        if dataset[y][x] == '0':
            trailends = []
            zeros.append([x,y])
            # print("doing",x,y)
            dfs(x,y)
            score += len(trailends)
# print(zeros)
print("part 1",score)
time3=time.time()

def dfspart2(x,y):
    for neighbour in getneighbours(x,y):
        if dataset[neighbour[1]][neighbour[0]] != '.':
            if int(dataset[neighbour[1]][neighbour[0]]) - int(dataset[y][x]) == 1:
                if dataset[neighbour[1]][neighbour[0]] == '9':
                    # if [neighbour[0],neighbour[1]] not in trailends:
                    trailends.append([neighbour[0],neighbour[1]])
                else:
                    dfspart2(neighbour[0],neighbour[1])

# print("###############")
# print("starting part 2")

trailends = []
score = 0
for y in range(h):
    for x in range(w):
        if dataset[y][x] == '0':
            trailends = []
            zeros.append([x,y])
            # print("doing",x,y)
            dfspart2(x,y)
            score += len(trailends)
print("part 2:",score)

time4=time.time()

print("read in time:",time2-time1)
print("part 1 time :", time3-time2)
print("part 2 time :", time4-time3)