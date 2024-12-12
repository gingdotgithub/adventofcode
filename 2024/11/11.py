import time
import functools
import sys
sys.setrecursionlimit(2500)

time1=time.time()
with open('11.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
time2=time.time()

parts = dataset[0].split(" ")
blinks = 25
for i in range(blinks):
    x = 0
    while x < len(parts):
        if parts[x] == '0':
            parts[x] = '1'
        elif len(parts[x]) & 1 == 0:
            mid = int(len(parts[x])/2)
            parta = str(int(parts[x][:mid]))
            partb = str(int(parts[x][mid:]))
            parts[x] = parta
            parts.insert(x+1,partb)
            x+=1
        else:
            parts[x] = str(int(parts[x])*2024)
        x+=1
    print("doing round",i+1)
    i+=1

print("part1",len(parts))
time3 = time.time()

print("## part 2 begins")
parts = dataset[0].split(" ")
time4 = time.time()

@functools.cache
def processit(total,val,depth):
    if depth == 75:
        return 1
    if val == '0':
        return processit(total,'1',depth+1)
    elif len(val) & 1 == 0:
        mid = int(len(val)/2)
        parta = processit(total,val[:mid], depth+1)
        partb = processit(total,str(int(val[mid:])), depth+1)
        return parta+partb
    else:
        return processit(total,str(int(val)*2024),depth+1)

total = 0
for part in parts:
    print("doing part",part)
    total+=processit(total, part,0)
print("part 2:",total)

time5 = time.time()

print("ingest:",time2-time1)
print("part 1:", time3-time2)
print("part 2:", time5-time4)