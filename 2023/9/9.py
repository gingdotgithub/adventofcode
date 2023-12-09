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
        return 0,0
    else:
        prevgap,nextgap = processSeq(nextSeq)
        return nextSeq[0]-prevgap,nextSeq[len(nextSeq)-1]+nextgap
    

with open('9.in') as f:
    data = f.readlines()

answer = 0
answer2 = 0
for row in data:
    sequence = list(map(int,row.strip().split()))
    prevgap,nextgap = processSeq(sequence)
    preval = sequence[0]-prevgap
    nextval = sequence[len(sequence)-1]+nextgap
    print(preval,nextval)
    answer+= nextval
    answer2+= preval

print("part 1",answer)
print("part 2",answer2)