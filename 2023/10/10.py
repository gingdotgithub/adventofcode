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
print(s)

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
    print("next node",nextnode,"next pipe",nextpipe,"direction",direction,"steps",steps)
    currnode = nextnode
print("part 1:",int(steps/2))




    
