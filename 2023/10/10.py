import time

pipes = {
    "|" : [-1,0,1,0], #N E S W
    "-" : [0,1,0,-1],
    "F" : [0,1,1,0],
    "L" : [-1,1,0,0],
    "J" : [-1,0,0,-1],
    "7" : [0,0,1,-1],
    "S" : [0,1,1,0]
}

with open('10.in') as f:
    pipemap = f.readlines()

starttime = time.time()
#find S
mainpipe = {}
s = (-1,-1)
for y in range(0,len(pipemap)):
    pipemap[y] = pipemap[y].strip()
    for x in range(0,len(pipemap[y])):
        if pipemap[y][x] == 'S':
            s = (x,y)
            break
    if s[0] > -1:
        break
mainpipe[s] = pipes['F']
#print(s)

nextnode = (-1,-1)
currnode = s
direction = (1,0)
steps = 0
while nextnode != s:
    nextnode = (currnode[0]+direction[0],currnode[1]+direction[1])
    nextpipe = pipemap[nextnode[1]][nextnode[0]]
    nextx = pipes[nextpipe][1]+pipes[nextpipe][3]+direction[0]
    nexty = pipes[nextpipe][0]+pipes[nextpipe][2]+direction[1]
    direction = nextx,nexty
    steps+=1
    #print("next node",nextnode,"next pipe",nextpipe,"direction",direction,"steps",steps)
    currnode = nextnode
    mainpipe[currnode] = nextpipe
endtime = time.time()
print("part 1:",int(steps/2))
print("timing:", endtime-starttime)
print(mainpipe)

inside = set()
outside = set()
####### part 2 ########

def floodfill(start):
    newset = set()
    tocheck = set()
    tocheck.add(start)
    isinside = True
    print("floodfilling from:",start)
    while len(tocheck) > 0:
        node = tocheck.pop()
        for y in range(node[1]-1,node[1]+2):
            for x in range(node[0]-1,node[0]+2):
                if x < 0 or x >= len(pipemap[0]) or y < 0 or y > len(pipemap):
                    isinside = False
                else:
                    checking = (x,y)
                    if checking not in mainpipe.keys() and checking not in inside and checking not in outside and checking not in newset:
                        print("checking",checking)
                        newset.add(checking)
                        tocheck.add(checking)
    print("first check:",newset,"is inside is",isinside)
    if isinside:
        doublecheck = newset.pop()
        newset.add(doublecheck)
        print("doublechecking",doublecheck)
        count = 0
        for x in range (0,doublecheck[0]):
            y = doublecheck[1]
            if (x,y) in mainpipe:
                print("found some pipe", (x,y), "is",mainpipe[(x,y)])
                if mainpipe[(x,y)] in set(["|","J","L"]):
                    print("its clash pipe")
                    count+=1 
        if count%2 == 0:
            isinside = False
    print("group found:",newset, "and isinside is ",isinside)
    return newset, isinside

for y in range(0,len(pipemap)):
    for x in range(0,len(pipemap[y])):
        if ((x,y) not in mainpipe.keys()) and ((x,y) not in inside) and ((x,y) not in outside):
            newset, isinside = floodfill((x,y))
            if isinside:
                inside.update(newset)
            else:
                outside.update(newset)

print("inside: ", sorted(inside))
print("part 2:",len(inside))
            
    
