import time

data = open('22.in').read().splitlines()
starttime = time.time()

def brickhit(b1,b2):
    if max(b1[0],b2[0]) <= min(b1[3],b2[3]) and max(b1[1],b2[1]) <= min(b1[4],b2[4]):
        return True
    return False

bricks = []
for brick in data:
    brick = brick.split("~")
    brick[0] = list(map(int,brick[0].split(",")))
    brick[1] = list(map(int,brick[1].split(",")))
    bricks.append([*brick[0],*brick[1]])
bricks.sort(key=lambda brick: brick[2])
print(bricks)

count = 0
for brick in bricks:
    lowest = 1
    for checkbrick in bricks[0:count]:
        if brickhit(brick,checkbrick):
            lowest = max(lowest,checkbrick[5] + 1)
    brick[5] -= brick[2]-lowest
    brick[2] = lowest
    count+=1

bricks.sort(key=lambda brick: brick[2])
print(bricks)

hasbricksontopof = {}
hasbricksunder = {}

n = 0
for brickabove in bricks:
    m = 0
    for brickbelow in bricks[0:n]:
        if brickhit(brickabove,brickbelow) and brickbelow[5] == brickabove[2]-1:
            if m not in hasbricksontopof:
                hasbricksontopof[m] = set()
            hasbricksontopof[m].add(n)
            if n not in hasbricksunder:
                hasbricksunder[n] = set()
            hasbricksunder[n].add(m)
        m+=1
    n+=1

print(hasbricksontopof) 
print(hasbricksunder)

zappable = set()
answer = 0
for brickID in range(0,len(bricks)):
    print("doing brick",brickID)
    if brickID in hasbricksontopof.keys():
        print("brick",brickID,"is under",hasbricksontopof[brickID])
        allsupported = True
        for bID in hasbricksontopof[brickID]:
            print("brick",bID,"is on top of",len(hasbricksunder[bID]),"bricks")
            if len(hasbricksunder[bID]) < 2:
                allsupported = False
        if allsupported:
            print("adding one")
            answer+=1
            zappable.add(brickID)
    else:
        print("nothing on top, so adding one")
        answer+=1
        zappable.add(brickID)

print("part 1",answer)

answer2=0
for brickID in range(0,len(bricks)):
    falling = [brickID]
    if brickID not in zappable:
        print("starting with brick",brickID)
        fallcheck = [brickID]
        while len(fallcheck) > 0:
            bID = fallcheck.pop(0)
            print("checking brick",bID)
            if bID in hasbricksontopof:
                [fallcheck.append(newbrick) for newbrick in hasbricksontopof[bID] if newbrick not in fallcheck]
                print("addings bricks above",hasbricksontopof[bID])
            notsupported = True
            if bID in hasbricksunder:
                print("checking supporting bricks",hasbricksunder[bID])
                for brick in hasbricksunder[bID]:
                    if brick not in falling:
                        notsupported = False
                if notsupported:
                    falling.append(bID)
                    print("added to falling",falling)
    falling.remove(brickID)
    print(falling)
    answer2+=len(falling)
print("part 2:",answer2)
