vents = []
xmax = 0
ymax = 0

while True:
    newline = input()
    if newline == '':
        break
    vent = newline.split(' -> ')
    ventline = [int(x) for x in vent[0].split(',')] + [int(x) for x in vent[1].split(',')]
    if ventline[0] > xmax or ventline[2] > xmax:
        xmax = max(ventline[0], ventline[1])
    if ventline[1] > ymax or ventline[3] > ymax:
        ymax = max(ventline[1], ventline[3])
    vents.append(ventline)

print(vents)
print(str(xmax) + " - " + str(ymax))
seabed = []
for x in range(ymax+1):
    seabed.append([0]*(xmax+1))
print(seabed)

for ventline in vents:
    print(ventline)
    if ventline[0] == ventline[2]:
        for y in range(min(ventline[1],ventline[3]),max(ventline[1],ventline[3])+1):
            print(str(ventline[0]) + "," + str(y))
            seabed[ventline[0]][y]+=1
            for seabedrow in seabed:
                print(seabedrow)
    elif ventline[1] == ventline[3]:
        for x in range(min(ventline[0],ventline[2]),max(ventline[0],ventline[2])+1):
            print(str(x) + "," + str(ventline[1]))
            seabed[x][ventline[1]]+=1
            for seabedrow in seabed:
                print(seabedrow)
    #print(seabed)

ventsum = 0
for seabedline in seabed:
    ventsum+=seabedline.count(2)

print(ventsum)

    