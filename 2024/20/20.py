import time

minsave = 100
with open('20.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
    
dirs = [(0,-1),(1,0),(0,1),(-1,0)]
ns = []
ne = []
grid = []
gridpoints = {}
for y in range(len(dataset)):
    if 'S' in dataset[y]:
        ns = (dataset[y].find('S'),y)
    if 'E' in dataset[y]:
        ne = (dataset[y].find('E'),y)
    grid.append(list(dataset[y]))

# print(grid)
# print("ns",ns,"ne",ne)
time1 = time.time()
todo = []
visited = []
def findpoints():
    global todo, visited,gridpoints,grid,dirs
    while len(todo) > 0:
        nn = todo.pop(0)
        # print(nn)
        cost = nn[1]
        if nn[0] == ne:
            gridpoints[ne] = cost
            visited.append(ne)
            return True
        else:
            visited.append(nn[0])
            gridpoints[nn[0]] = cost
        for dir in dirs:
            nextn = (nn[0][0]+dir[0],nn[0][1]+dir[1])
            if (grid[nextn[1]][nextn[0]] == '.' or grid[nextn[1]][nextn[0]] == 'E') and nextn not in visited:
                todo.append([nextn,cost+1])

def part1():
    global gridpoints,dirs,cheats
    tocheck = list(gridpoints.keys())
    visited = []
    for x in range(len(tocheck)-2):
        nn = tocheck[x]
        visited.append(nn)
        for dir in dirs:
            # if (nn[0]+dir[0],nn[1]+dir[1]) not in tocheck:
            nextn = (nn[0]+(dir[0]*2),nn[1]+(dir[1]*2))
            if nextn in tocheck and nextn not in visited:
                cheatdist = gridpoints[nextn]-gridpoints[nn]-2
                if cheatdist > 0:
                    if cheatdist not in cheats.keys():
                        cheats[cheatdist] = []
                    cheats[cheatdist].append((nn,nextn))
    count = 0
    for cheat in cheats:
        if cheat >= minsave:
            count+=len(cheats[cheat])
    return count
    
cheats = {}
todo.append([ns,0])
findpoints()
print("processd the path...")
time2 = time.time()
# print(gridpoints)
print("Part 1:",part1())
time3 = time.time()


def part2():
    global gridpoints,dirs,cheats
    tocheck = list(gridpoints.keys())
    for x in range(len(tocheck)-2):
        a = tocheck[x]
        posstargets = tocheck[x+2:]
        for b in posstargets:
            mandist = getdist(a,b)
            pathdist = gridpoints[b]-gridpoints[a]
            # print(mandist,a,b,pathdist)
            if mandist <= 20 and mandist < pathdist:
                cheatdist = pathdist - mandist
                if cheatdist not in cheats.keys():
                    cheats[cheatdist] = []
                cheats[cheatdist].append((a,b))
    count = 0
    for cheat in cheats:
        if cheat >= minsave:
            count+=len(cheats[cheat])
    return count
                

def getdist(a,b):
    return abs(b[0]-a[0])+abs(b[1]-a[1])

cheats = {}
print("Part 2:",part2())
# for cheat in cheats:
    # print(cheat,len(cheats[cheat]),cheats[cheat],"\n")
time4 = time.time()
print("Process grid:",time2-time1)
print("Part 1 time: ",time3-time2)
print("Part 2 time: ",time4-time3)