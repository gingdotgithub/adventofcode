import json
cuboids = {}
oncount = 0

def create_cuboid_data(stringput):
    c = []
    sign = 0
    parts = stringput.split()
    if parts[0]=="on":
        sign = 1
    else:
        sign = -1
    c.append([])
    dimensions = parts[1].split(",")
    for d in dimensions:
        c.append(list(map(int, d[2:].split('..'))))
    #volume = (c[1][1]+1-c[1][0])*(c[2][1]+1-c[2][0])*(c[3][1]+1-c[3][0])
    #c.append(volume)
    return c, sign

#detects the amount of c1 that is in c2
def detect_intersection(c1, c2):
    x = [max(c1[1][0], c2[1][0]),min(c1[1][1], c2[1][1])]
    y = [max(c1[2][0], c2[2][0]),min(c1[2][1], c2[2][1])]
    z = [max(c1[3][0], c2[3][0]),min(c1[3][1], c2[3][1])]
    return [x,y,z]

while True:
    newline = input()
    if newline == '':
        break
    cuboidstr, sign = create_cuboid_data(newline)
    cuboids[str(cuboidstr)] = sign

donecuboids = {}
for c in cuboids.keys():
    toadd = {}
    print("doing "+str(c))
    for dc in donecuboids.keys():
        myarray = json.loads(dc)
        intersect = detect_intersection(json.loads(c),myarray)
        if intersect[0][0] <= intersect[0][1] and intersect[1][0] <= intersect[1][1] and intersect[2][0] <= intersect[2][1]:
            newc = []
            newc.append([])
            newc.append(intersect[0])
            newc.append(intersect[1])
            newc.append(intersect[2])
            #volume = (newc[1][1]+1-newc[1][0])*(newc[2][1]+1-newc[2][0])*(newc[3][1]+1-newc[3][0])
            #newc.append(volume)
            if str(newc) not in toadd.keys():
                toadd[str(newc)] = 0
            toadd[str(newc)] -= donecuboids[dc]
    if cuboids[c] == 1:
        toadd[str(c)] = cuboids[c]
    for ta in toadd.keys():
        if ta not in donecuboids.keys():
            donecuboids[ta] = 0
        donecuboids[ta] += toadd[ta]

for n in donecuboids.keys():
    print(n + " - " + str(donecuboids[n]))
    c = json.loads(n)
    oncount+=(donecuboids[n]*(c[1][1]+1-c[1][0])*(c[2][1]+1-c[2][0])*(c[3][1]+1-c[3][0]))
print(oncount)