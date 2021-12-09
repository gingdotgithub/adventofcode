heightmap = []
sumoflowpoints = 0

while True:
    newline = input()
    if newline == '':
        break
    intmap = map(int, newline)
    heightmap.append(list(intmap))

for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        placefound = True
        if x > 0:
            if heightmap[y][x] >= heightmap[y][x-1]:
                placefound = False
        if x < len(heightmap[y])-1:
            if heightmap[y][x] >= heightmap[y][x+1]:
                placefound = False
        if y > 0:
            if heightmap[y][x] >= heightmap[y-1][x]:
                placefound = False
        if y < len(heightmap)-1:
            if heightmap[y][x] >= heightmap[y+1][x]:
                placefound = False
        if placefound:
            print (str(x)+","+str(y)+" = "+str(heightmap[y][x]))
            sumoflowpoints = sumoflowpoints + 1 + heightmap[y][x]

print(str(sumoflowpoints))
    