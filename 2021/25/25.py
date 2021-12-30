ECs = []
SCs = []
xlen = 0
ylen = 0

y = 0
while True:
    newline = list(input())
    if newline == []:
        ylen = y
        break
    xlen = len(newline)
    for x in range(xlen):
        if newline[x] == 'v':
            SCs.append([x,y])
        if newline[x] == '>':
            ECs.append([x,y])
    y+=1

stepcount = 0
movecount = 1
while movecount > 0:
    movecount = 0
    newECs = []
    newSCs = []
    for (ecx,ecy) in ECs:
        ecxp = (ecx+1)%xlen
        if [ecxp,ecy] not in ECs and [ecxp,ecy] not in SCs:
            movecount+=1
            newECs.append([ecxp,ecy])
        else:
            newECs.append([ecx,ecy])
    ECs = newECs
    for (scx,scy) in SCs:
        scyp = (scy+1)%ylen
        if [scx,scyp] not in ECs and [scx,scyp] not in SCs:
            movecount+=1
            newSCs.append([scx,scyp])
        else:
            newSCs.append([scx,scy])
    SCs = newSCs
    print("Step "+str(stepcount)+" - "+str(movecount)+" moved.")
    stepcount+=1

print(stepcount)




