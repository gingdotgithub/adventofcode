from time import process_time
starttime = 0.0
vents = {}
xmax = 0
ymax = 0

while True:
    newline = input()
    starttime = process_time()
    if newline == '':
        break
    vent = newline.split(' -> ')
    ventline = [int(x) for x in vent[0].split(',')] + [int(x) for x in vent[1].split(',')]
    if ventline[0] == ventline[2]:
        for y in range(min(ventline[1],ventline[3]),max(ventline[1],ventline[3])+1):
            newcoord = str(ventline[0])+","+str(y)
            if newcoord in vents.keys():
                vents[newcoord] += 1
            else:
                vents[newcoord] = 1
    elif ventline[1] == ventline[3]:
        for x in range(min(ventline[0],ventline[2]),max(ventline[0],ventline[2])+1):
            newcoord = str(x)+","+str(ventline[1])
            if newcoord in vents.keys():
                vents[newcoord] += 1
            else:
                vents[newcoord] = 1
    else:
        ventlinestartx = ventline[0]
        ventlinestarty = ventline[1]
        while True:
            newcoord = str(ventlinestartx)+","+str(ventlinestarty)
            if newcoord in vents.keys():
                vents[newcoord] += 1
            else:
                vents[newcoord] = 1
            if ventlinestartx == ventline[2]:
                break
            if ventlinestartx < ventline[2]:
                ventlinestartx+=1
            else:
                ventlinestartx-=1
            if ventlinestarty < ventline[3]:
                ventlinestarty+=1
            else:
                ventlinestarty-=1
        

print(vents)
ventcount = [coord for coord, count in vents.items() if count >= 2]
print(len(ventcount))
print(process_time()-starttime)