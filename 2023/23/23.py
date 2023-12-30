import time
import sys

sys.setrecursionlimit(10000)
data = open('23.in').read().splitlines()
starttime = time.time()

sx,sy = (1,0)
ex,ey = (len(data[0])-2,len(data)-1)
visited = set()
POIs = set()
graph = {}

def findPOIs():
    for y in range(1,len(data)-1):
        for x in range(1,len(data[0])-1):
            neighbours = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            if data[y][x] == '#':
                continue
            pathoptions = 0
            for nx,ny in neighbours:
                if data[ny][nx] != "#":
                    pathoptions+=1
            if pathoptions >= 3:
                POIs.add((x,y))
            
def contractEdges():
    for px,py in POIs:
        todo = [(0,px,py)]
        seen = set()
        while len(todo) > 0:
            #print(todo)
            dist,x,y = todo.pop(0)    
            neighbours = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            notallowed = ["<","^",">","v"] #used in part 1
            if (x,y) != (px,py) and (x,y) in POIs:
                if (px,py) not in graph.keys():
                    graph[(px,py)] = {}
                graph[(px,py)][(x,y)] = dist
                continue
            for possstep in range(0,len(neighbours)):
                nextstep = neighbours[possstep]
                #print(possstep,nextstep)
                if 0 < nextstep[0] < len(data) and 0 < nextstep[1] < len(data) and nextstep not in seen:
                    nextval = data[nextstep[1]][nextstep[0]]
                    if nextval != "#":# and nextval != notallowed[possstep]: #this bit makes it part 1 or part 2
                        todo.append((dist+1,nextstep[0],nextstep[1]))
                        seen.add(nextstep)
            

def findpathNew(point,depth):
    returnval = 0
    for neighbour in graph[point]:
        if neighbour == (ex,ey):
            print("found an end",depth+1)
            return depth + graph[point][neighbour]
        if neighbour not in visited:
            visited.add(neighbour)
            answer = findpathNew(neighbour,depth+graph[point][neighbour])
            visited.remove(neighbour)
            if answer > returnval:
                returnval = answer
    return returnval


def findpathOld(sx,sy,depth):
    #route.add((sx,sy))
    steps = [(sx+1,sy),(sx,sy+1),(sx-1,sy),(sx,sy-1)]
    notallowed = ["<","^",">","v"]
    returnval = 0
    for possstep in range(0,len(steps)):
        nextstep = steps[possstep]
        nextval = data[nextstep[1]][nextstep[0]]
        if nextstep == (ex,ey):
            print("found an end",depth+1)
            #f = input("?")
            return depth+1
        if nextstep not in visited and nextval != "#" and nextval != notallowed[possstep]: # in [".","v","^","<",">"]:
            #print("going",nextstep, "which is",nextval)
            visited.add(nextstep)
            answer = findpathOld(nextstep[0],nextstep[1],depth+1)
            visited.remove(nextstep)
            if answer > returnval:
                returnval = answer
    return returnval
    
# print((ex,ey))
# print(len(data[0]))
# print("part 1 timing:",time.time()-starttime)
# print("part 1:",findpathOld(sx,sy,0))

findPOIs()
POIs.add((sx,sy))
POIs.add((ex,ey))
#print(sorted(POIs))
contractEdges()
#print("graph:")
#for gkey in sorted(graph):
#    print(gkey,graph[gkey])
print("part 2:",findpathNew((sx,sy),0))
print("part 2 timing:",time.time()-starttime)