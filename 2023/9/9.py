import time

def processSeq(sequence):
    nextSeq = []
    allZero = True
    for x in range(0,len(sequence)-1):
        nextitem = sequence[x+1]-sequence[x]
        if nextitem != 0:
            allZero = False
        nextSeq.append(nextitem)
    if allZero:
        return 0
    else:
        nextgap = processSeq(nextSeq)
        return nextSeq[len(nextSeq)-1]+nextgap
    

with open('9.in') as f:
    data = f.readlines()

answer = 0
for row in data:
    sequence = list(map(int,row.strip().split()))
    nextgap = processSeq(sequence)
    nextval = sequence[len(sequence)-1]+nextgap
    print(nextval)
    answer+= nextval

print("part 1",answer)