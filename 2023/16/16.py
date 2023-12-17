import time

with open('16.in') as f:
    grid = f.readlines()

for row in range(0,len(grid)):
    grid[row] = grid[row].strip()

def part1(starttile):
    nexttiles=[starttile] #thats x,y position and direction x,y
    beenthere = set()
    energized = set()
    moving = True

    while moving:
        while len(nexttiles) > 0:
            # f = input("what?")
            #print("queue",nexttiles)
            tile = nexttiles.pop(0)
            #print("doing",tile)
            if tile not in beenthere:
                beenthere.add(tile)
                if tile[0] < 0 or tile[1] < 0 or tile[0] >= len(grid[0]) or tile[1] >= len(grid):
                    n = 1
                    #print(tile,"is off grid")
                else:
                    if (tile[0],tile[1]) not in energized:
                        energized.add((tile[0],tile[1]))
                    tval = grid[tile[1]][tile[0]]
                    if tval == ".":
                        nexttiles.append((tile[0]+tile[2],tile[1]+tile[3],tile[2],tile[3]))
                    elif tval == "-":
                        if tile[2] != 0:
                            nexttiles.append((tile[0]+tile[2],tile[1]+tile[3],tile[2],tile[3]))
                        else:
                            nexttiles.append((tile[0]-1,tile[1],-1,0))
                            nexttiles.append((tile[0]+1,tile[1],1,0))
                    elif tval == "|":
                        if tile[3] != 0:
                            nexttiles.append((tile[0]+tile[2],tile[1]+tile[3],tile[2],tile[3]))
                        else:
                            nexttiles.append((tile[0],tile[1]-1,0,-1))
                            nexttiles.append((tile[0],tile[1]+1,0,1))
                    elif tval == "/":
                        if tile[2] == 1:
                            nexttiles.append((tile[0],tile[1]-1,0,-1))
                        elif tile[2] == -1:
                            nexttiles.append((tile[0],tile[1]+1,0,1))
                        elif tile[3] == 1:
                            nexttiles.append((tile[0]-1,tile[1],-1,0))
                        else:
                            nexttiles.append((tile[0]+1,tile[1],1,0))
                    elif tval == "\\":
                        if tile[2] == 1:
                            nexttiles.append((tile[0],tile[1]+1,0,1))
                        elif tile[2] == -1:
                            nexttiles.append((tile[0],tile[1]-1,0,-1))
                        elif tile[3] == 1:
                            nexttiles.append((tile[0]+1,tile[1],1,0))
                        else:
                            nexttiles.append((tile[0]-1,tile[1],-1,0))
                    else:
                        n = 1
                        #print("no more to do")
        moving = False
    #print(energized)
    return len(energized)
starttime = time.time()
print("part 1:",part1((0,0,1,0)))
endtime = time.time()
print("timing",endtime-starttime)

starttime = time.time()
bestanswer = 0
for x in range(0,len(grid[0])):
    print("starting at",(x,0,0,1))
    thisanswer = part1((x,0,0,1))
    if thisanswer > bestanswer:
        bestanswer = thisanswer
    print("starting at",(x,len(grid)-1,0,-1))
    thisanswer = part1((x,len(grid)-1,0,-1))
    if thisanswer > bestanswer:
        bestanswer = thisanswer
for y in range(0,len(grid)):
    print("starting at",(0,y,1,0))
    thisanswer = part1((0,y,1,0))
    if thisanswer > bestanswer:
        bestanswer = thisanswer
    print("starting at",(len(grid[0])-1,y,-1,0))
    thisanswer = part1((len(grid[0])-1,y,-1,0))
    if thisanswer > bestanswer:
        bestanswer = thisanswer
print("part 2:",bestanswer)
endtime = time.time()
print("part 2 timing:",endtime-starttime)
        
