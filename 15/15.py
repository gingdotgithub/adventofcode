from collections import defaultdict
room = []

while True:
    newline = input()
    if newline == '':
        break
    roomline = list(map(int,list(newline)))
    room.append(roomline)

distances = defaultdict(lambda:float("inf"))
distances["0,0"] = 0

for y in range (len(room)):
    for x in range(len(room[0])):
        if (x-1) >= 0:
            if distances[str(x-1)+","+str(y)] + room[y][x] < distances[str(x)+","+str(y)]:
                distances[str(x)+","+str(y)] = distances[str(x-1)+","+str(y)] + room[y][x]
        if (y-1) >= 0:
            if distances[str(x)+","+str(y-1)] + room[y][x] < distances[str(x)+","+str(y)]:
                distances[str(x)+","+str(y)] = distances[str(x)+","+str(y-1)] + room[y][x]

for cell in distances.keys():
    print("distance to " + cell + " = " + str(distances[cell]))
