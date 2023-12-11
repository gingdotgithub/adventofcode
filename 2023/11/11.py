import time
import re

with open('11.in') as f:
    galaxy = f.readlines()


starttime = time.time()
exrows = []
excols = list(range(0,len(galaxy[0])-1))
planets = []

for y in range(0,len(galaxy)):
    galaxy[y] = galaxy[y].strip()
    if len(set(galaxy[y])) == 1:
        exrows.append(y)
    else:
        for x in re.finditer('#',galaxy[y]):
            planets.append((x.start(),y))
            if x.start() in excols:
                excols.remove(x.start())

print(planets)
print(exrows)
print(excols)

answer = 0
for m in range(0,len(planets)):
    for n in range(m+1,len(planets)):
        minx = min(planets[n][0],planets[m][0])
        maxx = max(planets[n][0],planets[m][0])
        miny = min(planets[n][1],planets[m][1])
        maxy = max(planets[n][1],planets[m][1])
        # diffx = maxx-minx
        # diffy = planets[n][1] - planets[m][1]
        dist = (maxx-minx)+(maxy-miny)
        print(planets[m],"to",planets[n],"is",dist)
        dist += len(list(filter(lambda x: x > minx and x < maxx,excols)))
        dist += len(list(filter(lambda y: y > miny and y < maxy,exrows)))
        #dist += len(list(excols[excols>minx and excols<maxx]))
        #dist += len(list(exrows[exrows>miny and exrows<maxy]))
        print(planets[m],"to",planets[n],"is now",dist)
        answer+=dist

print("part 1",answer)