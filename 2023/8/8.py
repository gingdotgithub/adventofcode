import re

with open('8.in') as f:
    data = f.readlines()

mapnetwork = {}
steps = list(data[0].strip())
for node in range(2,len(data)):
    nodedetail = re.sub(r'[^\w\s]','',data[node])
    nodeparts = nodedetail.split()
    mapnetwork[nodeparts[0]] = [nodeparts[1],nodeparts[2]]
print(mapnetwork)

notfound = True
step = 0
currnode = "AAA"
print(steps)
while notfound:
    nextstep = steps[step%len(steps)]
    print("going",nextstep)
    if nextstep == "R":
        nextnode = mapnetwork[currnode][1]
    else:
        nextnode = mapnetwork[currnode][0]
    print(nextnode)
    if nextnode == "ZZZ":
        notfound = False
    else:
        currnode = nextnode
    step+= 1
print("part 1:", step)
