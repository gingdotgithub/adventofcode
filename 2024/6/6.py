with open('6.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

rocks = []
starter = ()

h = len(dataset)
w = len(dataset[0])
for y in range(h):
    for x in range(w):
        if dataset[y][x] == "#":
            rocks.append((x,y))
        if dataset[y][x] == "^":
            starter = (x,y)

dirs = [(0,-1),(1,0),(0,1),(-1,0)]
original = starter

inbox = True
visited = []
path = []
visited.append(starter)
path.append(starter+dirs[0])
# print(path)
while inbox:
    # print(starter)
    next = (starter[0]+dirs[0][0],starter[1]+dirs[0][1])

    if next[0] >=0 and next[0] < w and next[1] >= 0 and next[1] < h:
        if next in rocks:
            dirs.append(dirs.pop(0))
            next = (starter[0]+dirs[0][0],starter[1]+dirs[0][1])
        starter = next
        if starter not in visited:
            visited.append(starter)
        if starter+dirs[0] not in path:
            path.append(starter+dirs[0])
    else:
        inbox = False

           
print("part1:",len(visited))
print(path)

#part 2
guardpath = visited
newrocks = []
for x in range(0,len(guardpath)):
    print("trying",(guardpath[x][0],guardpath[x][1]))
    rocks.append((guardpath[x][0],guardpath[x][1]))
    starter = original
    dirs = [(0,-1),(1,0),(0,1),(-1,0)]
    inbox = True
    looping = False
    path=[starter+dirs[0]]

    while inbox and not looping:
        next = (starter[0]+dirs[0][0],starter[1]+dirs[0][1])+dirs[0]
        if next[0] >=0 and next[0] < w and next[1] >= 0 and next[1] < h:
            while (next[0],next[1]) in rocks:
                dirs.append(dirs.pop(0))
                next = (starter[0]+dirs[0][0],starter[1]+dirs[0][1])+dirs[0]
            starter = next
            if starter in path:
                if (guardpath[x][0],guardpath[x][1]) not in newrocks:
                    newrocks.append((guardpath[x][0],guardpath[x][1]))
                print("we're looping!")
                looping = True
            else:
                path.append(starter)

        else:
            inbox = False
        # print(path)

    rocks.remove((guardpath[x][0],guardpath[x][1]))
#         rocks.append((path[x][0],path[x][1]))
#         _,_,clash = walkit(starter)
#         if clash:
#             newrockcount+=1
#             newrocks.append((path[x][0],path[x][1]))
#             print("rock at",(path[x][0],path[x][1]))
#         rocks.remove((path[x][0],path[x][1]))
#         x+=1
print(newrocks)
print("part2:",len(newrocks))

    