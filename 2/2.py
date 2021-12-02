x,y = 0,0
while True:
    line = input()
    if line == '':
        break
    direction, distance = line.split()
    if direction == "forward":
        x+= int(distance)
    elif direction == "up":
        y-= int(distance)
    elif direction == "down":
        y+= int(distance)

print("answer: " + str(x*y))