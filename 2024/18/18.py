import time
import heapq

h = 7
w = 7
n = 12
with open('18.test') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
    dataset = [tuple(map(int,line.split(","))) for line in dataset]

dirs = [(0,-1),(1,0),(0,1),(-1,0)]
# print(dataset)
visited = []
time1=time.time()

def part1():
    global visited
    visited = []
    openlist = []
    heapq.heappush(openlist,(0.0,(0,0)))

    while len(openlist) > 0:
        # print("todo",openlist)
        nn = heapq.heappop(openlist)
        if nn[1] not in visited:
            visited.append(nn[1])
            # print("visited",visited)
            # print("doing",nn)
            # test=input()
            for dir in dirs:
                newx = nn[1][0]+dir[0]
                newy = nn[1][1]+dir[1]
                if newx == w-1 and newy == h-1:
                    return nn[0]+1
                if 0 <= newx < w and 0 <= newy < h and (newx,newy) not in visited and (newx,newy) not in dataset[:n]:
                    # print("adding",(newx,newy))
                    heapq.heappush(openlist,(nn[0]+1,(newx,newy)))
    return 0

time2 = time.time()        
print("Part 1:",part1())

def part2():
    global n
    global visited
    firstvisited = visited.copy()
    startn = n
    for x in range(startn+1,len(dataset)):
        # if dataset[x] in firstvisited:
        n = x
        if part1() == 0:
            return x

answer = part2()
print("Part 2 is n = ",answer)
time3 = time.time()
print("Part 2:", dataset[answer-1])

print("Part 1 time:",time2-time1)
print("Part 2 time:",time3-time2)
