import sys

inputs = input().split(',')
newline = input()
boards = []
currentinput = 0


#function checks if a row sums to 5, or if a column sums to 5, or returns false
def checkboard(boardtocheck):
    for row in boardtocheck:
        if sum(row.values()) == 5:
            return True
    #check each column (by index of each row).
    for y in range(5):
        mysum = 0
        for row in boardtocheck:
            myvalues = list(row.values())
            mysum+=myvalues[y]
        if mysum == 5:
                return True
    return False

#function finds the keys for all 0 values in the board dicts, and sums the keys
def calculateanswer(boardtocalc):
    answersum = 0
    for row in boardtocalc:
        for (key, value) in row.items():
            if value == 0:
                answersum+=int(key)
    return answersum*int(currentinput)

#MAIN CODE
#loop to read in all the boards
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

#boardcounts keeps a score of how many nums found in board
boardcounts = [0]*len(boards)
#lastcheckcounts keeps a record of what value it checked last (to only check again if changed)
lastcheckcounts = [0]*len(boards)
#for part 2 of day 4, this keeps a count of how many boards are left
countboardsleft = len(boards)

print(boardcounts)
print(lastcheckcounts)

#main loop goes through the input numbers of the bingo
for x in inputs:
    #updates 'currentinput' for the final calculation of the answer
    currentinput = x
    #currboard is an ID for looping through the boards
    currboard = -1
    #this loop essentially looks for any number in each grid that matches the bingo number,
    #and then sets its value to 1 if found
    for board in boards:
        currboard+=1
        for row in board:
            if x in row:
                row[x] = 1
                if boardcounts[currboard] >= 0:
                    boardcounts[currboard]+=1
    print(boardcounts)

    #check if we are down to one board. if so, calculate the main answer to part 2 of day 4
    if countboardsleft == 1:
        for finalboard in range(len(boardcounts)):
            if boardcounts[finalboard] > 0:
                print("answer = " + str(calculateanswer(boards[finalboard])) + "curr item: " + currentinput)
                sys.exit()
    #else cycle through the boards to find any to remove
    else:
        for y in range(len(boardcounts)):
            #if its a candidate board, and its changed since last check
            if boardcounts[y] > 5 and boardcounts[y] > lastcheckcounts[y]:
                lastcheckcounts[y] = boardcounts[y]
                #check if its a winning board and remove it
                winningboard = checkboard(boards[y])
                if winningboard == True and len(boards) > 1:
                    #setting values to -1 indicates its won and now out of the game
                    boardcounts[y] = -1
                    lastcheckcounts[y] = -1
                    #and decreases the count of boards left
                    countboardsleft -= 1
        