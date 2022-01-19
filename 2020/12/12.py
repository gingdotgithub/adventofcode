instructions = []
location = [0,0]
heading = 1
headings = ['N','E','S','W']

while True:
    newline = input()
    if newline == '':
        break
    else:
        instructions.append([newline[0:1],int(newline[1:])])

print(instructions)

for inst,val in instructions:
    if inst == 'F':
        location[heading%2] += (val * (1 if heading < 2 else -1))
    elif inst == 'L':
        heading = int(heading - (val/90))%4
    elif inst == 'R':
        heading = int(4+(heading + (val/90)))%4
    else:
        direction = headings.index(inst)
        location[direction%2] += (val * (1 if direction < 2 else -1))
    print(location)

print(abs(location[0])+abs(location[1]))