heightmap = []
basins = {}
#localbasin = []

def explorebasin(x,y):
    localbasin = [[x,y]]
    countcheck = 0
    while countcheck < len(localbasin):
        checkx = localbasin[countcheck][0]
        checky = localbasin[countcheck][1]
        newx,newy = checkcoord(checkx,checky-1,localbasin)
        if newx != -1:
            localbasin.append([newx,newy])
        newx,newy = checkcoord(checkx,checky+1,localbasin)
        if newx != -1:
            localbasin.append([newx,newy])
        newx,newy = checkcoord(checkx-1,checky,localbasin)
        if newx != -1:
            localbasin.append([newx,newy])
        newx,newy = checkcoord(checkx+1,checky,localbasin)
        if newx != -1:
            localbasin.append([newx,newy])
        countcheck+=1
    if len(localbasin) == 63:
        print(sorted(localbasin))
    basins[str(x)+","+str(y)] = countcheck
        


def checkcoord(x,y, mybasin=[]):
    placefound = True
    if x == 49 and y == 93:
        mytest = True
    if x in range(len(heightmap[0])) and y in range(len(heightmap)) and [x,y] not in mybasin and heightmap[y][x] != 9:
        if x > 0 and [x-1,y] not in mybasin:
            if heightmap[y][x] > heightmap[y][x-1]:
                placefound = False
        if x < len(heightmap[y])-1 and [x+1,y] not in mybasin:
            if heightmap[y][x] > heightmap[y][x+1]:
                placefound = False
        if y > 0 and [x,y-1] not in mybasin:
            if heightmap[y][x] > heightmap[y-1][x]:
                placefound = False
        if y < len(heightmap)-1 and [x,y+1] not in mybasin:
            if heightmap[y][x] > heightmap[y+1][x]:
                placefound = False
    else:
        placefound = False
    if placefound:
        return x,y
    else:
        return -1,-1

while True:
    newline = input()
    if newline == '':
        break
    intmap = map(int, newline)
    heightmap.append(list(intmap))

for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        newx,newy = checkcoord(x,y)
        if newx >= 0:
            #print (str(x)+","+str(y)+" = "+str(heightmap[y][x]))
            basins[str(x)+","+str(y)] = 1

#print(basins)

for coordstr in basins.keys():
    coord = list(map(int,coordstr.split(",")))
    explorebasin(coord[0],coord[1])

print(basins)        

sortedbasins = sorted(basins.values(),reverse=True)
print(sortedbasins)
print(str(sortedbasins[0]*sortedbasins[1]*sortedbasins[2]))
    