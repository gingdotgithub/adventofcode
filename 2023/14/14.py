import numpy as np

with open('14.in') as f:
    data = f.readlines()

for x in range(0,len(data)):
    print(data[x])
    data[x] = list(data[x].strip())
#print(data)

def printcols(cols):
    for row in cols:
        print("".join(row))

def rotate(cols,way):
    npcols = np.array(cols)
    cols = np.rot90(npcols,way).tolist()
    return cols


def calcweight(cols):
    answer = 0
    for x in range(0,len(cols)):
        for y in range(0,len(cols[x])):
            if cols[x][y] == "O":
                answer += (len(cols[x])-y)
    return answer


def tilt(cols):
    for x in range(0,len(cols)):
        dots = []
        for y in range(0,len(cols[x])):
            # print("checking",x,y,cols[x][y])
            if cols[x][y] == ".":
                dots.append(y)
            elif cols[x][y] == "#":
                dots = []
            elif cols[x][y] == "O":
                if len(dots) > 0:
                    lowestdot = dots.pop(0)
                    cols[x][lowestdot] = "O"
                    cols[x][y] = "."
                    dots.append(y)
    #printcols(cols)
    return cols

# Part 1
# data = rotate(data,1)
# data = tilt(data)
# answer = calcweight(data)
# print("part 1:",answer)

# Part 2
colsdone = [tuple(map(tuple,data))]
colsseen = set(tuple(map(tuple,data)))
data = rotate(data,1)
notseen = True
counter = 0
#for n in range(0,1000000000):
while notseen == True:
    counter += 1
    print("doing",counter)
    for m in range(0,4):
        data = tilt(data)
        data = rotate(data,-1)
    
    printcols(data)
    print("its weight is:",calcweight(data))
    tupleofdata = tuple(map(tuple,data)) 
    #probably have should have just worked with tuples from the start. 
    if tupleofdata in colsseen:
        notseen = False
    else:
        colsseen.add(tupleofdata)
        colsdone.append(tupleofdata)
        print("its weight is still",calcweight(data))
        

first = colsdone.index(tupleofdata)
looplength = counter-first
print(counter, first, len(colsdone),looplength)

indexofresult = first+((1000000000-first)%looplength)
print(indexofresult)
print("part 2:", calcweight(colsdone[indexofresult]))
