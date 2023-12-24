import time
import sys

sys.setrecursionlimit(10000)
data = open('23.in').read().splitlines()
starttime = time.time()

sx,sy = (1,0)
ex,ey = (len(data[0])-2,len(data)-1)
visited = set()

def findpath(sx,sy,depth):
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
        if nextstep not in visited and nextval != "#": # and nextval != notallowed[possstep]: # in [".","v","^","<",">"]:
            #print("going",nextstep, "which is",nextval)
            visited.add(nextstep)
            answer = findpath(nextstep[0],nextstep[1],depth+1)
            visited.remove(nextstep)
            if answer > returnval:
                returnval = answer
    return returnval
    
# print((ex,ey))
# print(len(data[0]))
print("part 1:",findpath(sx,sy,0))
print("part 1 timing:",time.time()-starttime)