octopi = []
countflashes = 0

def printboard():
    for row in octopi:
        print(row)
    print("")

def processflash(x,y):
    global countflashes
    newval = octopi[y][x] + 1
    octopi[y][x] = newval % 10
    if newval == 10:
        flashing.append([x,y])
        countflashes += 1

while True:
    readline = input()
    if readline == "":
        break
    octopi.append(list(map(int,list(readline))))

printboard()
for step in range(100):
    flashing = []
    for x in range(len(octopi[0])):
        for y in range(len(octopi)):
            processflash(x,y)
    
    for octoflash in flashing:
        x = octoflash[0]
        y = octoflash[1]
        for i in range(-1,2):
            for j in range(-1,2):
                if x+i >= 0 and x+i < len(octopi[0]) and y+j >= 0 and y+j < len(octopi) and [x+i,y+j] not in flashing:
                    processflash(x+i,y+j)
                
    if step < 10 or step%10 == 0:
        printboard()
print(str(countflashes))
