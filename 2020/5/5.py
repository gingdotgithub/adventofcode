maxseatID = 0
seatIDs = []

while True:
    newline = input()
    if newline == '':
        break
    rowdata = newline[0:7]
    coldata = newline[7:]
    rowdata = rowdata.replace("B","1")
    rowdata = rowdata.replace("F","0")
    coldata = coldata.replace("R","1")
    coldata = coldata.replace("L","0")
    seatID = (int(rowdata,2)*8)+int(coldata,2)
    seatIDs.append(seatID)
    if seatID > maxseatID:
        maxseatID = seatID

print(maxseatID)
seatIDs = sorted(seatIDs)
for x in range(len(seatIDs)):
    if x>8 and x<924:
        if seatIDs[x-1] != seatIDs[x]-1:
            print(seatIDs[x]-1)
