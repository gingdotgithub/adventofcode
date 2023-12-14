
with open('14.in') as f:
    data = f.readlines()

cols = []
boulders=[]
rocks=[]
for x in range(0,len(data)):
    print(data[x])
    
    data[x] = list(data[x].strip())
    for y in range(0,len(data[x])):
        if len(cols) <= y:
            cols.append([])
        cols[y].append(data[x][y])
        # if data[x][y] == "#":
        #     rocks.append((y,x))
    #print(cols[x])


print(cols)
# print(rocks)

answer = 0
for x in range(0,len(cols)):
    dots = []
    for y in range(0,len(cols[x])):
        print("checking",x,y,cols[x][y])
        if cols[x][y] == ".":
            dots.append(y)
        elif cols[x][y] == "#":
            dots = []
        elif cols[x][y] == "O":
            if len(dots) > 0:
                lowestdot = dots.pop(0)
                cols[x][lowestdot] = "O"
                answer+=(len(cols[x])-lowestdot)
                print("mover, gets",len(cols[x])-lowestdot)
                cols[x][y] = "."
                dots.append(y)
            else:
                answer+=(len(cols[x])-y)
                print("non-move, gets",len(cols[x])-y)

print("part 1:",answer)
        
