import time

data = open('18.in').read().splitlines()
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

print(edge)
print(points)
upgroup = 0
downgroup = 0
for x in range(0,len(points)-1):
    upgroup+=(points[x][1]*points[x+1][0])
    downgroup+=(points[x][0]*points[x+1][1])

fullarea = 0.5*abs(upgroup-downgroup) #shoelace
#but shoelace includes parts of the boundaries, because we are looking at a grid. 
#so need to use picks theorem to get the internal bits only
internalarea = fullarea-(edge/2)+1 # had to look this up
print("part 1:",edge+internalarea)