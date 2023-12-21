import time
import re

data = open('21.in').read().splitlines()
starttime = time.time()

rocks = set()
start = (0,0)
for y in range(0,len(data)):
    for x in [i.start() for i in re.finditer('(?=#)',data[y])]:
        rocks.add((x,y))
    if "S" in data[y]:
        start = (data[y].index("S"),y)
print(start)

def expand(fromnodes,steps):
    steps -= 1
    newnodes = set()
    for node in fromnodes:
        print(node)
        if node[0]-1 >= 0 and (node[0]-1,node[1]) not in rocks:
            newnodes.add((node[0]-1,node[1]))
        if node[0]+1 < len(data[0]) and (node[0]+1,node[1]) not in rocks:
            newnodes.add((node[0]+1,node[1]))
        if node[1]-1 >= 0 and (node[0],node[1]-1) not in rocks:
            newnodes.add((node[0],node[1]-1))
        if node[1]+1 < len(data) and (node[0],node[1]+1) not in rocks:
            newnodes.add((node[0],node[1]+1))
    
    if steps > 0:
        return expand(newnodes,steps)
    print(sorted(newnodes))
    return len(newnodes)

print("part 1:",expand({start},64))