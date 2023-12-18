import time

data = open('18.in').read().splitlines()

def part1():
    starttime = time.time()
    points = [(0,0)]
    edge = 0 #starting with edge
    for x in range(0,len(data)):
        data[x] = data[x].split()
        if data[x][0] == 'R':
            points.append((points[x][0]+int(data[x][1]),points[x][1]))
        elif data[x][0] == 'L':
            points.append((points[x][0]-int(data[x][1]),points[x][1]))
        elif data[x][0] == 'U':
            points.append((points[x][0],points[x][1]+int(data[x][1])))
        elif data[x][0] == 'D':
            points.append((points[x][0],points[x][1]-int(data[x][1])))
        edge+=int(data[x][1])

    #print(edge)
    #print(points)
    upgroup = 0
    downgroup = 0
    for x in range(0,len(points)-1):
        upgroup+=(points[x][1]*points[x+1][0])
        downgroup+=(points[x][0]*points[x+1][1])

    fullarea = 0.5*abs(upgroup-downgroup) #shoelace
    #but shoelace includes parts of the boundaries, because we are looking at a grid. 
    #so need to use picks theorem to get the internal bits only
    internalarea = fullarea-(edge/2)+1 # had to look this up
    endtime = time.time()
    print("part 1:",edge+internalarea)
    print("part 1 timing:",endtime-starttime)

def part2():
    starttime = time.time()
    points = [(0,0)]
    edge = 0 #starting with edge
    for x in range(0,len(data)):
        lhd = len(data[x][2])
        direction = data[x][2][lhd-2:lhd-1]
        #print(direction)
        hexdata = int(data[x][2][lhd-7:lhd-2],16)
        #print(hexdata)
        if direction == '0':
            points.append((points[x][0]+int(hexdata),points[x][1]))
        elif direction == '2':
            points.append((points[x][0]-int(hexdata),points[x][1]))
        elif direction == '3':
            points.append((points[x][0],points[x][1]+int(hexdata)))
        elif direction == '1':
            points.append((points[x][0],points[x][1]-int(hexdata)))
        edge+=int(hexdata)

    #print(edge)
    #print(points)
    upgroup = 0
    downgroup = 0
    for x in range(0,len(points)-1):
        upgroup+=(points[x][1]*points[x+1][0])
        downgroup+=(points[x][0]*points[x+1][1])

    fullarea = 0.5*abs(upgroup-downgroup) #shoelace
    #but shoelace includes parts of the boundaries, because we are looking at a grid. 
    #so need to use picks theorem to get the internal bits only
    internalarea = fullarea-(edge/2)+1 # had to look this up
    endtime = time.time()
    print("part 2:",edge+internalarea)
    print("part 2 timing:",endtime-starttime)

part1()
part2()