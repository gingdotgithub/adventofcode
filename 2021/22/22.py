cuboids = []
space = [[-50,50],[-50,50],[-50,50]]
oncount = 0

def create_cuboid_data(stringput):
    c = []
    parts = stringput.split()
    c.append(parts[0])
    dimensions = parts[1].split(",")
    for d in dimensions:
        c.append(list(map(int, d[2:].split('..'))))
    volume = (c[1][1]+1-c[1][0])*(c[2][1]+1-c[2][0])*(c[3][1]+1-c[3][0])
    c.append(volume)
    return c

def create_set(c):
    cset = set(())
    for x in range(c[0][0],c[0][1]+1):
        for y in range(c[1][0],c[1][1]+1):
            for z in range(c[2][0],c[2][1]+1):
                cset.add(str([x,y,z]))
    return cset


#detects the amount of c1 that is in c2
def detect_intersection(c1, c2):
    #x,y,z = 0,0,0
    #if c1[1] >= c2[0] and c1[0] <= c2[1]:
    x = [max(c1[1][0], c2[1][0]),min(c1[1][1], c2[1][1])]
    y = [max(c1[2][0], c2[2][0]),min(c1[2][1], c2[2][1])]
    z = [max(c1[3][0], c2[3][0]),min(c1[3][1], c2[3][1])]
    return [x,y,z]

def in_space(c):
    if space[0][0] <= c[1][0] <= space[0][1]:
        if space[0][0] <= c[1][1] <= space[0][1]:
            if space[1][0] <= c[2][0] <= space[1][1]:
                if space[1][0] <= c[2][1] <= space[1][1]:
                    if space[2][0] <= c[3][0] <= space[2][1]:
                        if space[2][0] <= c[3][1] <= space[2][1]:
                            return True
    return False

while True:
    newline = input()
    if newline == '':
        break
    cuboids.append(create_cuboid_data(newline))

donecuboids = []
while len(cuboids) > 0:
    c = cuboids.pop(0)
    if in_space(c):
        vol = c[4]
        cset = create_set([c[1],c[2],c[3]])
        #check in 5050 range
        for dc in donecuboids:
            intersect=detect_intersection(c,dc)
            iset=create_set(intersect)
            if dc[0] == "on":
                cset.difference_update(iset)
            else:
                cset.update(iset)
        
        donecuboids.append(c)
        if c[0] == "on":
            oncount+=len(cset)
        else:
            oncount-=(vol-len(cset))
        if oncount < 0:
            oncount = 0
        

print(cuboids)
print(oncount)