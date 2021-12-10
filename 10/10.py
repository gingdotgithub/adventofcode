expectedouts = {"[" : "]", "{" : "}", "(" : ")", "<" : ">"}
outscores = {")" : 3, "]" : 57, "}" : 1197, ">": 25137}
chunkstack = []
totalscore = 0

while True:
    newline = input()
    if newline == '':
        break
    readline = list(newline)
    while len(readline) > 0:
        currentitem = readline.pop(0)
        if currentitem in expectedouts.keys():
            chunkstack.append(currentitem)
        else:
            lastopener = chunkstack.pop()
            if currentitem != expectedouts[lastopener]:
                print(newline + " - Expected " + expectedouts[lastopener] + ", but found " + currentitem + "instead.")
                totalscore += outscores[currentitem]

print(str(totalscore))