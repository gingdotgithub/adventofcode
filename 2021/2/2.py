x,y,aim = 0,0,0
while True:
    line = input()
    if line == '':
        break
    direction, distance = line.split()
    if direction == "forward":
        x+= int(distance)
        y+= aim*int(distance)
    elif direction == "up":
        aim-= int(distance)
    elif direction == "down":
        aim+= int(distance)

print("answer: " + str(x*y))