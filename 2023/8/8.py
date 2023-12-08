import re
import math

with open('8.in') as f:
    data = f.readlines()

startnodes = {}
mapnetwork = {}
steps = list(data[0].strip())
for node in range(2,len(data)):
    nodedetail = re.sub(r'[^\w\s]','',data[node])
    nodeparts = nodedetail.split()
    mapnetwork[nodeparts[0]] = [nodeparts[1],nodeparts[2]]
    if nodeparts[0][2] == "A":
        startnodes[nodeparts[0]] = 0
print(mapnetwork)
print(startnodes)
print(steps)

for sn in startnodes.keys():
    notfound = True
    step = 0
    currnode = sn
    while notfound:
        nextstep = steps[step%len(steps)]
        print("going",nextstep)
        if nextstep == "R":
            nextnode = mapnetwork[currnode][1]
        else:
            nextnode = mapnetwork[currnode][0]
        print(nextnode)
        if nextnode[2] == "Z":
            notfound = False
        currnode = nextnode
        step+= 1
    startnodes[sn] = step

depths = list(startnodes.values())
print("part 2:", math.lcm(*depths))
