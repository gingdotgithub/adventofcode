import time
import re

data = open('21.in').read().splitlines()
starttime = time.time()

rocks = set()
start = (0,0,0,0)
for y in range(0,len(data)):
    for x in [i.start() for i in re.finditer('(?=#)',data[y])]:
        rocks.add((x,y))
    if "S" in data[y]:
        start = (data[y].index("S"),y,0,0)
#print(start)
foundnodes = set()
newnodes = set()
cache = []
def expand(steps): #this is really inefficient and takes up to 12s+ to reach step 327.
    global foundnodes,newnodes
    for step in range(steps,0,-1):
        print("doing step",steps-step)
        newnodes.clear()
        for node in foundnodes:
            #print("from",node)
            if node[0]-1 >= 0: #and (node[0]-1,node[1]) not in rocks:
                candidate = (node[0]-1,node[1],node[2],node[3])
            else:
                candidate = (len(data[0])-1,node[1],node[2]-1,node[3])
                #print("looped",node,"to",candidate)
            if (candidate[0],candidate[1]) not in rocks:
                newnodes.add(candidate)
                #print("added",candidate)

            if node[0]+1 < len(data[0]): # and (node[0]+1,node[1]) not in rocks:
                candidate = (node[0]+1,node[1],node[2],node[3])
            else:
                candidate = (0,node[1],node[2]+1,node[3])
                #print("looped",node,"to",candidate)
            if (candidate[0],candidate[1]) not in rocks:
                newnodes.add(candidate)
                #print("added",candidate)

            if node[1]-1 >= 0:# and (node[0],node[1]-1) not in rocks:
                candidate = (node[0],node[1]-1,node[2],node[3])
            else:
                candidate = (node[0],len(data)-1,node[2],node[3]-1)
                #print("looped",node,"to",candidate)
            if (candidate[0],candidate[1]) not in rocks:
                newnodes.add(candidate)
                #print("added",candidate)
            
            if node[1]+1 < len(data):# and (node[0],node[1]+1) not in rocks:
                candidate = (node[0],node[1]+1,node[2],node[3])
            else:
                candidate = (node[0],0,node[2],node[3]+1)
                #print("looped",node,"to",candidate)
            if (candidate[0],candidate[1]) not in rocks:
                newnodes.add(candidate)
                #print("added",candidate)
        #print("new nodes",len(newnodes))
        foundnodes = newnodes.copy()
        if steps-step+1 in [65, 196, 327]: #this is on the sole premise that someone figured out that the answer follows a quadratic equation only because the input is the way it is.  #thanks colm
            cache.append(len(foundnodes))

foundnodes.add(start)
expand(327)
x = int(26501365 / len(data))
a,b,c = cache
answer = a+x*(b-a+(x-1)*((a+c)/2-b)) #one day id like to understand this as well as achieve it. :-D
endtime = time.time()
print("part 2:",answer)
print("part 2 timing:",endtime-starttime)

#637537341306357