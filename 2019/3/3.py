from numpy import *

def processWire(w):
    x = 0
    y = 0
    neww = []
    #neww.append((x,y))
    for part in w:
        print(part[1])
        for n in range(0,int(part[1:])):
            if part[0] == "R":
                x = x+1
            elif part[0] == "D":
                y = y-1
            elif part[0] == "L":
                x = x-1
            else:
                y = y+1
            neww.append((x,y))
    return neww.copy()


wire1 = []
wire2 = []
with open('3.in') as f:
    wire1 = f.readline().split(",")
    wire2 = f.readline().split(",")

wire1 = processWire(wire1)
wire2 = processWire(wire2)

intersections = list(set(wire1) & set(wire2))
mandists = []
print(intersections)
for i in intersections:
    mandists.append(abs(i[0]) + abs(i[1]))
mandists.sort()
print(mandists)