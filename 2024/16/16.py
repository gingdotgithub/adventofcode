import time
import math
import heapq

time1=time.time()
with open('16.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

grid = []
ns = []
ne = []
facing = (1,0)
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

print("start",ns,"end",ne)
print(grid)
# def hval(src):
#     a = src[0]
#     b = src[1]
#     x = ne[0]
#     y = ne[1]
#     return ((x-a)**2 + (y-b)**2)**0.5

def printgrid():
    for row in grid:
        print("".join(row))

def part1(facing):
    openlist = []
    visited = []
    heapq.heappush(openlist,(0.0,ns[0],ns[1],facing))

    while len(openlist) > 0:
        nn = heapq.heappop(openlist)
        visited.append([nn[1],nn[2]])
        facing = nn[3]
        # printgrid()
        # print("checking",nn)
        # test = input()

        for dir in dirs[facing]:
            newx = nn[1]+dir[0]
            newy = nn[2]+dir[1]
            if [newx,newy] == ne:
                return nn[0]+dir[2]
            if [newx,newy] not in visited and grid[newy][newx] == '.':
                heapq.heappush(openlist,(nn[0]+dir[2],newx,newy,(dir[0],dir[1])))
    
print("part 1:",part1(facing))
