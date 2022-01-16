import copy
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
    if y > 0:
        if x > 0:
            Occupied += 1 if seating[y-1][x-1] == '#' else 0
        Occupied += 1 if seating[y-1][x] == '#' else 0
        if x < w-1:
            Occupied += 1 if seating[y-1][x+1] == '#' else 0
    if x > 0:
        Occupied += 1 if seating[y][x-1] == '#' else 0
    if x < w-1:
        Occupied += 1 if seating[y][x+1] == '#' else 0
    if y < h-1:
        if x > 0:
            Occupied += 1 if seating[y+1][x-1] == '#' else 0
        Occupied += 1 if seating[y+1][x] == '#' else 0
        if x < w-1:
            Occupied += 1 if seating[y+1][x+1] == '#' else 0
    return Occupied

def print_seating():
    global seating
    for row in seating:
        print("".join(row))
    print("")

#print_seating()

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
            if seating[y][x] == '#' and Occupied >= 4:
                newseating[y][x] = "L" 
                change_count+=1
    seating = copy.deepcopy(newseating)
    count_loops+=1
    #print_seating()

Occupied = 0
for x in range(len(seating[0])):
    for y in range(len(seating)):
        if seating[y][x] == '#':
            Occupied += 1

print(count_loops)
print(Occupied)