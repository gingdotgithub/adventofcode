import time
import re
import math

time1=time.time()
with open('14.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

def processrobots():
    for robot in dataset:
        robot = re.split('[=|,| ]',robot)
        robot.remove("v")
        robot.remove("p")
        robots.append(list(map(int,robot)))

def moverobots(clicks):
    for robot in robots:
        robot[0] = (robot[0]+(robot[2]*clicks))%w
        robot[1] = (robot[1]+(robot[3]*clicks))%h
# print(finallocations)

def findquads():
    for robot in robots:
        if robot[0] < int(w/2) and robot[1] < int(h/2):
            quads[0]+=1
        elif robot[0] > int(w/2) and robot[1] < int(h/2):
            quads[1]+=1
        elif robot[0] < int(w/2) and robot[1] > int(h/2):
            quads[2]+=1
        elif robot[0] > int(w/2) and robot[1] > int(h/2):
            quads[3]+=1

robots = []
clicks = 100
w=101
h=103
quads = [0,0,0,0]
robots=[]
processrobots()
moverobots(clicks)
findquads()
time2 = time.time()
print("part 1:",math.prod(quads))

grid = []
def makegrid():
    grid = []
    for y in range(h):
        line = ["."]*w
        grid.append(line)
    # grid[10][5] = "X"
    for robot in robots:
        grid[robot[1]][robot[0]] = 'X'
    # print(grid)
    return grid

def checkfortree():
    linescount=0
    for line in grid:
        linestr = "".join(line)
        if "XXXXX" in linestr:
            linescount+=1
        if linescount > 5:
            return True

# printgrid()
robots=[]
processrobots()
clicks = 0
while True:
    clicks+=1
    moverobots(1)
    grid = makegrid()
    view = checkfortree()
    # print(grid)
    if view:
        print(grid)
        print("clicks was",clicks)
        break
time3 = time.time()
print("Part 2",clicks)
print("Part 1 time:",time2-time1)
print("Part 2 time:",time3-time2)
