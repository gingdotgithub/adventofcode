import time
import heapq
import sys

sys.setrecursionlimit(100000)

time1=time.time()
with open('16.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

grid = []
ns = []
ne = []
facing = (1,0)
visited = {}
dirs = {
    (1,0)  : [[0,-1,1001],[1,0,1],[0,1,1001]],
    (0,1)  : [[1,0,1001],[0,1,1],[-1,0,1001]],
    (-1,0) : [[0,1,1001],[-1,0,1],[0,-1,1001]],
    (0,-1) : [[1,0,1001],[0,-1,1],[-1,0,1001]]
}


for y in range(len(dataset)):
    if 'E' in dataset[y]:
        ne = [dataset[y].index('E'),y]
    if 'S' in dataset[y]:
        ns = [dataset[y].index('S'),y]
    grid.append(list(dataset[y]))

# print("start",ns,"end",ne)
# print(grid)

def printgrid():
    for row in grid:
        print("".join(row))

def part1(facing):
    openlist = []
    global visited
    heapq.heappush(openlist,(0.0,ns[0],ns[1],facing))

    while len(openlist) > 0:
        nn = heapq.heappop(openlist)
        if (nn[1],nn[2]) not in visited.keys() or ((nn[1],nn[2]) in visited.keys() and nn[0] < visited[(nn[1],nn[2])]):
            visited[(nn[1],nn[2])] = nn[0]
        facing = nn[3]
        # printgrid()
        # print("checking",nn)
        # test = input()

        for dir in dirs[facing]:
            newx = nn[1]+dir[0]
            newy = nn[2]+dir[1]
            if [newx,newy] == ne:
                return nn[0]+dir[2]
            print(nn[0])
            if (newx,newy) not in visited.keys() and grid[newy][newx] == '.':
                heapq.heappush(openlist,(nn[0]+dir[2],newx,newy,(dir[0],dir[1])))

time2 = time.time()    
bestdistance = part1(facing)
time3 = time.time()    
print("visited:",visited, len(visited))
uniquevis = set(visited)
print("unique",len(uniquevis))
print("part 1:",bestdistance)
# test = input()
goodseats = set()
dfsvisited = []
def part2(nn,facing,cost):
    global visited
    global dfsvisited
    global goodseats
    global bestdistance
    if nn not in dfsvisited:
        dfsvisited.append(nn)
        # print("doing",nn,dfsvisited)
        if grid[nn[1]][nn[0]] == 'E':
            dfsvisited.remove(nn)
            # print("cost",cost,"best",bestdistance)
            # test = input()
            if cost == bestdistance:
                # print("cost",cost,"best",bestdistance)
                return True
            else:
                return False
        if cost > bestdistance:
            # print("too long now",cost)
            dfsvisited.remove(nn)
            return False
        if cost > visited[(nn[0],nn[1])]+1000:
            # print("gone a suboptimal route to here")
            dfsvisited.remove(nn)
            return False
        for dir in dirs[facing]:
            newx = nn[0]+dir[0]
            newy = nn[1]+dir[1]
            # if (newx,newy) in visited.keys() and (grid[newy][newx] == '.' or grid[newy][newx] == 'E'): #and (newx,newy) in visited
            if (newx,newy) in visited.keys() or grid[newy][newx] == 'E':
                result = part2((newx,newy),(dir[0],dir[1]),cost+dir[2])
                if result:
                    goodseats.update(dfsvisited)
                    
        dfsvisited.remove(nn)
    # return result

part2((ns[0],ns[1]),facing,0)
time4 = time.time()
# print(goodseats,len(goodseats))       
print("Part 2",len(goodseats)+1)
print("part 1 time:",time3-time2)
print("Part 2 time:",time4-time3)
