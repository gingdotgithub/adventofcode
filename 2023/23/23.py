import time
import sys

sys.setrecursionlimit(10000)
data = open('23.test').read().splitlines()
starttime = time.time()

sx,sy = (1,0)
ex,ey = (len(data[0])-2,len(data)-1)

def findpath(sx,sy,route):
    route.add((sx,sy))
    steps = [(sx+1,sy),(sx,sy+1),(sx-1,sy),(sx,sy-1)]
    notallowed = ["<","^",">","v"]
    returnval = 0
    for possstep in range(0,len(steps)):
        nextstep = steps[possstep]
        nextval = data[nextstep[1]][nextstep[0]]
        if nextstep == (ex,ey):
            print("found an end",len(route),". max is now",returnval)
            #f = input("?")
            return len(route)
        if nextstep not in route and nextval != "#" and nextval != notallowed[possstep]: # in [".","v","^","<",">"]:
            #print("going",nextstep, "which is",nextval)
            answer = findpath(nextstep[0],nextstep[1],route.copy())
            if answer > returnval:
                returnval = answer
    return returnval
    
# print((ex,ey))
# print(len(data[0]))
print("part 1:",findpath(sx,sy,set()))
print("part 1 timing:",time.time()-starttime)