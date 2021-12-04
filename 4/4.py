import sys

inputs = input().split(',')
newline = input()
boards = []
currentinput = 0

def checkboard(boardtocheck):
    for row in boardtocheck:
        if sum(row.values()) == 5:
            return True
    for y in range(5):
        mysum = 0
        for row in boardtocheck:
            myvalues = list(row.values())
            print(myvalues)
            mysum+=myvalues[y]
        if mysum == 5:
                return True
    return False

def calculateanswer(boardtocalc):
    answersum = 0
    for row in boardtocalc:
        for (key, value) in row.items():
            if value == 0:
                answersum+=int(key)
    return answersum*int(currentinput)

while True:
    newboard = []
    newline = input()
    if newline == '':
        break
    newboard.append(dict.fromkeys(newline.split(),0))
    newboard.append(dict.fromkeys(input().split(),0))
    newboard.append(dict.fromkeys(input().split(),0))
    newboard.append(dict.fromkeys(input().split(),0))
    newboard.append(dict.fromkeys(input().split(),0))
    boards.append(newboard)
    newline = input()

print(boards)
boardcounts = [0]*len(boards)
lastcheckcounts = [0]*len(boards)

print(boardcounts)
print(lastcheckcounts)

for x in inputs:
    currentinput = x
    currboard = -1
    for board in boards:
        currboard+=1
        for row in board:
            if x in row:
                row[x] = 1
                boardcounts[currboard]+=1
    print(boardcounts)

    for y in range(len(boardcounts)):
        if boardcounts[y] > 5 and boardcounts[y] > lastcheckcounts[y]:
            lastcheckcounts[y] = boardcounts[y]
            found = checkboard(boards[y])
            if found == True:
                print("answer = " + str(calculateanswer(boards[y])))
                sys.exit()
        