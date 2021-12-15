import math

expectedouts = {"[" : "]", "{" : "}", "(" : ")", "<" : ">"}
fixscores = {")" : 3, "]" : 57, "}" : 1197, ">": 25137}
acscores = {")" : 1, "]" : 2, "}" : 3, ">": 4}
chunkstack = [] #main stack for processing
totalfixscore = 0 #for corrupted lines
completescore = 0 #for auto-completed lines
completescores = [] #to store and sort auto-completed scores

#read every line
while True:
    newline = input()
    if newline == '':
        break
    readline = list(newline)
    #process the line for corrupted items
    while len(readline) > 0:
        currentitem = readline.pop(0)
        #if its a left bracket, add it to the stack
        if currentitem in expectedouts.keys():
            chunkstack.append(currentitem)
        #else check that it matches the top item in the stack
        else:
            lastopener = chunkstack.pop()
            #if not, well - we found a currupted item. give it a score and add it to the total
            if currentitem != expectedouts[lastopener]:
                print(newline + " - Expected " + expectedouts[lastopener] + ", but found " + currentitem + "instead.")
                totalfixscore += fixscores[currentitem]
                chunkstack = [] #this clears the chunk stack so it doesnt get processed in the next section
                break

    #process any uncorrupted thus incomplete lines 
    #(remaining openers that need a close should be in the chunkstack)
    acitems = []
    completescore = 0
    while len(chunkstack) > 0:
        currentitem = chunkstack.pop()
        acitems.append(expectedouts[currentitem]) #just for printing out purposes
        completescore=(completescore*5)+acscores[expectedouts[currentitem]]
    if completescore > 0: #otherwise it would print out the 0s for unneeded lines and append zeros to the array
        print(''.join(acitems) + " - " + str(completescore) + " total points.")
        completescores.append(completescore)


print(str(totalfixscore))
completescores = sorted(completescores) #sort the autocompleted scores and print out the mid point
print(str(completescores[math.floor(len(completescores)/2)]))
