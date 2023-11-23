from numpy import *

def processWire(w):
    x = 0
    y = 0
    counter = 0
    neww = {}
    #neww.append((x,y)) - dont add the root, it becomes an intersection point
    for part in w:
        #print(part[1])
        for n in range(0,int(part[1:])):
            if part[0] == "R":
                x = x+1
            elif part[0] == "D":
                y = y-1
            elif part[0] == "L":
                x = x-1
            else:
                y = y+1
            counter = counter + 1
            if (x,y) not in neww.keys():
                neww[(x,y)] = counter
    return neww.copy()


def part1():
    mandists = []
    #print(intersections)
    for i in intersections:
        mandists.append(abs(i[0]) + abs(i[1]))
    mandists.sort()
    print("part 1: ", mandists[0])

def part2():
   stepdists = []
   for i in intersections:
       stepdists.append(wire1map[i] + wire2map[i])
   stepdists.sort()
   print("part 2: ", stepdists[0])


wire1 = []
wire2 = []
with open('3.in') as f:
    wire1 = f.readline().split(",")
    wire2 = f.readline().split(",")

wire1map = processWire(wire1)
wire2map = processWire(wire2)
intersections = list(set(wire1map.keys()) & set(wire2map.keys()))
part1()
part2()
