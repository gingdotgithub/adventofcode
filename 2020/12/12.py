instructions = []
location = [0,0]
heading = 1
headings = ['N','E','S','W']
waypoint = [10,1]

while True:
    newline = input()
    if newline == '':
        break
    else:
        instructions.append([newline[0:1],int(newline[1:])])

print(instructions)

for inst,val in instructions:
    if inst == 'F':
        location[0] += (waypoint[0] * val)
        location[1] += (waypoint[1] * val)
    elif inst == 'L':
        #heading = int(heading - (val/90))%4
        while val > 0:
            waypoint.append(waypoint.pop(0))
            waypoint[0]*=-1
            val-=90
    elif inst == 'R':
        #heading = int(4+(heading + (val/90)))%4
        while val > 0:
            waypoint.append(waypoint.pop(0))
            waypoint[1]*=-1
            val-=90
    else:
        direction = headings.index(inst)
        waypoint[(1+direction)%2] += (val * (1 if direction < 2 else -1))
    print(str(location) + " " + str(waypoint))

print(abs(location[0])+abs(location[1]))