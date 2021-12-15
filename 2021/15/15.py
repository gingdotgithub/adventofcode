from collections import defaultdict
from queue import PriorityQueue
room = []

while True:
    newline = input()
    if newline == '':
        break
    roomline = list(map(int,list(newline)))
    room.append(roomline)

distances = defaultdict(lambda:float("inf"))
distances["0,0"] = 0
visited = []
tovisit = PriorityQueue()
tovisit.put((0,"0,0"))


while not tovisit.empty():
    (distance,cell) = tovisit.get()
    visited.append(cell)
    cellsplit = cell.split(",")
    x = int(cellsplit[0])
    y = int(cellsplit[1])
    neighbour = str(x-1)+","+str(y)
    if (x-1) >= 0 and neighbour not in visited:
        newcost = distances[cell] + ((room[y%len(room)][(x-1)%len(room[0])]+(y//len(room))+((x-1)//len(room[0]))-1)%9)+1
        if newcost < distances[neighbour]:
            distances[neighbour] = newcost
            tovisit.put((newcost,neighbour))
    neighbour = str(x)+","+str(y-1)
    if (y-1) >= 0 and neighbour not in visited:
        newcost = distances[cell] + ((room[(y-1)%len(room)][x%len(room[0])]+((y-1)//len(room))+(x//len(room[0]))-1)%9)+1
        if newcost < distances[neighbour]:
            distances[neighbour] = newcost
            tovisit.put((newcost,neighbour))
    neighbour = str(x+1)+","+str(y)
    if (x+1) <len(room[0])*5 and neighbour not in visited:
        newcost = distances[cell] + ((room[y%len(room)][(x+1)%len(room[0])]+(y//len(room))+((x+1)//len(room[0]))-1)%9)+1
        if newcost < distances[neighbour]:
            distances[neighbour] = newcost
            tovisit.put((newcost,neighbour))
    neighbour = str(x)+","+str(y+1)    
    if (y+1) < len(room)*5 and neighbour not in visited:
        newcost = distances[cell] + ((room[(y+1)%len(room)][x%len(room[0])]+((y+1)//len(room))+(x//len(room[0]))-1)%9)+1
        if newcost < distances[neighbour]:
            distances[neighbour] = newcost
            tovisit.put((newcost,neighbour))

for cell in distances.keys():
    x,y = cell.split(",")
    if int(x)%10 == 9 and int(y)%10 == 9:
        print("distance to " + cell + " = " + str(distances[cell]))
