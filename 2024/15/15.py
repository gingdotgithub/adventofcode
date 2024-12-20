import time
import re
import math

time1=time.time()
with open('15.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

dirs = {}
dirs["<"] = [-1,0]
dirs["^"] = [0,-1]
dirs[">"] = [1,0]
dirs["v"] = [0,1]
grid = []
bot = []

def processgrid():
    instr = ""
    blankline = False
    x = 0
    for x in range(len(dataset)):
        if dataset[x] == "":
            blankline = True
        elif not blankline:
            grid.append(list(dataset[x]))
        else:
            instr+=dataset[x]
        x+=1

    instr = list(instr)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                bot = [x,y]
                break
    return instr,bot

instr,bot = processgrid()
# print(grid)
# print(instr)
# print(bot)

def move(loc,dir):
    # print(grid[loc[1]+dir[1]][loc[0]+dir[0]])
    if grid[loc[1]+dir[1]][loc[0]+dir[0]] == "#":
        # print("not moving")
        return False
    elif grid[loc[1]+dir[1]][loc[0]+dir[0]] == "O":
        if move([loc[0]+dir[0],loc[1]+dir[1]],dir):
            #swap
            grid[loc[1]][loc[0]],grid[loc[1]+dir[1]][loc[0]+dir[0]] = grid[loc[1]+dir[1]][loc[0]+dir[0]],grid[loc[1]][loc[0]]
            return True
        else:
            return False
    else:
        #swap
        grid[loc[1]][loc[0]],grid[loc[1]+dir[1]][loc[0]+dir[0]] = grid[loc[1]+dir[1]][loc[0]+dir[0]],grid[loc[1]][loc[0]]
        return True

def printgrid(grid):
    for row in grid:
        print("".join(row))

def part1(bot):
    for action in instr:
        if move(bot,dirs[action]):
            bot = [bot[0]+dirs[action][0],bot[1]+dirs[action][1]]
            # print("bot now at",bot)
        # printgrid()
        # temp = input()

def calcgps():
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                total+=((100*y)+x)
    return total


part1(bot)
# printgrid(grid)
time2 = time.time()
print("Part 1",calcgps())

######################
#### PART 2 Code #####
######################


def rebuildgrid():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                grid2[y].append("#")
                grid2[y].append("#")
            elif grid[y][x] == ".":
                grid2[y].append(".")
                grid2[y].append(".")
            elif grid[y][x] == "@":
                grid2[y].append("@")
                grid2[y].append(".")
            elif grid[y][x] == "O":
                grid2[y].append("[")
                grid2[y].append("]")
        if y != len(grid)-1:
            grid2.append([])
    
    for y in range(len(grid2)):
        for x in range(len(grid2[0])):
            if grid2[y][x] == "@":
                bot = [x,y]
                break
    return bot

grid = []
grid2 = [[]]
instr,bot = processgrid() #regen original state
bot = rebuildgrid() #as double wide, and return bot new location
# printgrid(grid2)

def move2(loc,dir):
    # print("next item is:",grid2[loc[1]+dir[1]][loc[0]+dir[0]])
    # printgrid(grid2)
    # test = input()
    if dir == dirs["<"] or dir == dirs[">"]:
        if grid2[loc[1]+dir[1]][loc[0]+dir[0]] != '.':
            move2([loc[0]+dir[0],loc[1]+dir[1]],dir)
        #swap
        grid2[loc[1]][loc[0]],grid2[loc[1]+dir[1]][loc[0]+dir[0]] = grid2[loc[1]+dir[1]][loc[0]+dir[0]],grid2[loc[1]][loc[0]]
        
    elif grid2[loc[1]+dir[1]][loc[0]+dir[0]] == '[':
        if grid2[loc[1]+dir[1]+dir[1]][loc[0]+dir[0]] != grid2[loc[1]+dir[1]][loc[0]+dir[0]]:
            move2([loc[0]+dir[0]+1,loc[1]+dir[1]],dir)
        move2([loc[0]+dir[0],loc[1]+dir[1]],dir)
        if grid2[loc[1]][loc[0]] == '[':#!= "@":
            #swap neighbour
            grid2[loc[1]][loc[0]+1],grid2[loc[1]+dir[1]][loc[0]+dir[0]+1] = grid2[loc[1]+dir[1]][loc[0]+dir[0]+1],grid2[loc[1]][loc[0]+1]
        #swap
        grid2[loc[1]][loc[0]],grid2[loc[1]+dir[1]][loc[0]+dir[0]] = grid2[loc[1]+dir[1]][loc[0]+dir[0]],grid2[loc[1]][loc[0]]
        
    elif grid2[loc[1]+dir[1]][loc[0]+dir[0]] == ']':
        if grid2[loc[1]+dir[1]+dir[1]][loc[0]+dir[0]] != grid2[loc[1]+dir[1]][loc[0]+dir[0]]:
             move2([loc[0]+dir[0]-1,loc[1]+dir[1]],dir)
        move2([loc[0]+dir[0],loc[1]+dir[1]],dir)
        if grid2[loc[1]][loc[0]] == ']': #!= "@":
            #swap neighbour
            grid2[loc[1]][loc[0]-1],grid2[loc[1]+dir[1]][loc[0]+dir[0]-1] = grid2[loc[1]+dir[1]][loc[0]+dir[0]-1],grid2[loc[1]][loc[0]-1]
        #swap
        grid2[loc[1]][loc[0]],grid2[loc[1]+dir[1]][loc[0]+dir[0]] = grid2[loc[1]+dir[1]][loc[0]+dir[0]],grid2[loc[1]][loc[0]]
    else:
        #swap
        grid2[loc[1]][loc[0]],grid2[loc[1]+dir[1]][loc[0]+dir[0]] = grid2[loc[1]+dir[1]][loc[0]+dir[0]],grid2[loc[1]][loc[0]]
        

def canmove2(loc,dir):
    if grid2[loc[1]+dir[1]][loc[0]+dir[0]] == '.':
        return True
    elif grid2[loc[1]+dir[1]][loc[0]+dir[0]] == '#':
        return False
    elif dir == dirs["<"] or dir == dirs[">"]:
        return canmove2([loc[0]+dir[0]+dir[0],loc[1]+dir[1]],dir)
    elif grid2[loc[1]+dir[1]][loc[0]+dir[0]] == '[':
        return canmove2([loc[0]+dir[0],loc[1]+dir[1]],dir) and canmove2([loc[0]+dir[0]+1,loc[1]+dir[1]],dir)
    elif grid2[loc[1]+dir[1]][loc[0]+dir[0]] == ']':
        return canmove2([loc[0]+dir[0],loc[1]+dir[1]],dir) and canmove2([loc[0]+dir[0]-1,loc[1]+dir[1]],dir)
    else:
        return False

def part2(bot):
    for action in instr:
        # print("action is",action)
        if canmove2(bot,dirs[action]):
            move2(bot,dirs[action])
            bot = [bot[0]+dirs[action][0],bot[1]+dirs[action][1]]
            # print("bot now at",bot)
        # printgrid(grid2)
        # temp = input()

def calcgps2():
    total = 0
    for y in range(len(grid2)):
        for x in range(len(grid2[0])):
            if grid2[y][x] == '[':
                total+=((100*y)+x)
    return total

part2(bot)
# printgrid(grid2)
time3 = time.time()
print("Part 2:",calcgps2())
print("Part 1 time:",time2-time1)
print("Part 2 time:",time3-time2)