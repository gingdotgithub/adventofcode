import copy
from collections import Counter
seating = []

while True:
    newline = input()
    if newline == '':
        break
    seating.append(list(newline))
w = len(seating[0])
h = len(seating)

def count_neighbours(x,y):
    global w, h, seating
    Occupied = 0
    sidesHit = Counter()
    visibleHit = Counter()
    n = 0
    while n < w and len(sidesHit) < 4 and len(visibleHit) < 8:
        if y-n > 0:
            if x-n > 0:
                if visibleHit[0] != 1 and seating[y-n-1][x-n-1] != '.':
                    Occupied += 1 if seating[y-n-1][x-n-1] == '#' else 0
                    visibleHit[0] = 1
            else:
                sidesHit[0] = 1
            if visibleHit[1] != 1 and seating[y-n-1][x] != '.':
                Occupied += 1 if seating[y-n-1][x] == '#' else 0
                visibleHit[1] = 1
            if x+n < w-1:
                if visibleHit[2] != 1 and seating[y-n-1][x+n+1] != '.':
                    Occupied += 1 if seating[y-n-1][x+n+1] == '#' else 0
                    visibleHit[2] = 1
            else:
                sidesHit[2] = 1
        else:
            sidesHit[3] = 1
        if x-n > 0:
            if visibleHit[4] != 1 and seating[y][x-n-1] != '.':
                Occupied += 1 if seating[y][x-n-1] == '#' else 0
                visibleHit[4] = 1
        if x+n < w-1:
            if visibleHit[5] != 1 and seating[y][x+n+1] != '.':
                Occupied += 1 if seating[y][x+n+1] == '#' else 0
                visibleHit[5] = 1
        if y+n < h-1:
            if x-n > 0:
                if visibleHit[6] != 1 and seating[y+n+1][x-n-1] != '.':
                    Occupied += 1 if seating[y+n+1][x-n-1] == '#' else 0
                    visibleHit[6] = 1
            if visibleHit[7] != 1 and seating[y+n+1][x] != '.':
                Occupied += 1 if seating[y+n+1][x] == '#' else 0
                visibleHit[7] = 1
            if x+n < w-1:
                if visibleHit[8] != 1 and seating[y+n+1][x+n+1] != '.':
                    Occupied += 1 if seating[y+n+1][x+n+1] == '#' else 0
                    visibleHit[8] = 1
        else:
            sidesHit[1] = 1
        n+=1
    return Occupied

def print_seating():
    global seating
    for row in seating:
        print("".join(row))
    print("")

print_seating()

change_count = 1
count_loops = 0
while change_count > 0:
    change_count = 0
    newseating = copy.deepcopy(seating)
    for x in range(len(seating[0])):
        for y in range(len(seating)):
            if seating[y][x] == '.':
                continue
            Occupied = count_neighbours(x,y)
            if seating[y][x] == 'L' and Occupied == 0:
                newseating[y][x] = "#"
                change_count+=1
            if seating[y][x] == '#' and Occupied >= 5:
                newseating[y][x] = "L" 
                change_count+=1
    seating = copy.deepcopy(newseating)
    count_loops+=1
    print_seating()

Occupied = 0
for x in range(len(seating[0])):
    for y in range(len(seating)):
        if seating[y][x] == '#':
            Occupied += 1

print(count_loops)
print(Occupied)