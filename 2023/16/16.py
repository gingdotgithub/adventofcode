with open('16.in') as f:
    grid = f.readlines()

for row in range(0,len(grid)):
    grid[row] = grid[row].strip()

nexttiles=[(0,0,1,0)] #thats x,y position and direction x,y
beenthere = []
energized = []
moving = True

while moving:
    while len(nexttiles) > 0:
        # f = input("what?")
        print("queue",nexttiles)
        tile = nexttiles.pop(0)
        print("doing",tile)
        if tile not in beenthere:
            beenthere.append(tile)
            if tile[0] < 0 or tile[1] < 0 or tile[0] >= len(grid[0]) or tile[1] >= len(grid):
                print(tile,"is off grid")
            else:
                if (tile[0],tile[1]) not in energized:
                    energized.append((tile[0],tile[1]))
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
                    print("no more to do")
    moving = False
                
print(energized)
print("part 1:",len(energized))
        
