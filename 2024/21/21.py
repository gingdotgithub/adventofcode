import time
import itertools
import functools
import sys
sys.setrecursionlimit(10000)

with open('21.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
    dataset = ["A"+line for line in dataset]
print(dataset)

time1 = time.time()
#################
#processing datastructures
#################

keyboard = [['7','8','9'],['4','5','6'],['1','2','3'],['_','0','A']]
keyplaces = {}
dirboard = [['_','^','A'],['<','v','>']]
dirplaces = {}

kbmoves = {}
for y in range(len(keyboard)):
    for x in range(len(keyboard[0])):
        key1 = keyboard[y][x]
        keyplaces[key1] = (x,y)
        if key1 == '_':
            continue
        for j in range(len(keyboard)):
            for i in range(len(keyboard[0])):
                key2 = keyboard[j][i]
                if key2 == '_':
                    continue
                kbmoves[key1+key2] = []
                hdist = i-x
                if hdist > 0:
                    kbmoves[key1+key2].append(['>']*hdist)
                elif hdist < 0:
                    kbmoves[key1+key2].append(['<']*abs(hdist))
                vdist = j-y
                if vdist < 0:
                    kbmoves[key1+key2].append(['^']*abs(vdist))
                elif vdist > 0:
                    kbmoves[key1+key2].append(['v']*abs(vdist))

# print(kbmoves)
for k in kbmoves.keys():
    if len(kbmoves[k]) > 1:
        buttons = kbmoves[k]
        newbuttons = []
        key1 = k[0]
        key2 = k[1]
        # print("key check",key1,key2,buttons)
        # print("keyplace1",keyplaces[key1])
        # print("keyplace2",keyplaces[key2])
        if not(keyplaces[key1][0] == 0 and keyplaces[key2][1] == 3):
            newbuttons.append(buttons[1]+buttons[0])
        if not(keyplaces[key2][0] == 0 and keyplaces[key1][1] == 3):
            newbuttons.append(buttons[0]+buttons[1])
        kbmoves[k] = newbuttons.copy()
        # print("now",newbuttons)
        # input()
    


dirmoves = {}
for y in range(len(dirboard)):
    for x in range(len(dirboard[0])):
        dir1 = dirboard[y][x]
        dirplaces[dir1] = (x,y)
        if dir1 == '_':
            continue
        for j in range(len(dirboard)):
            for i in range(len(dirboard[0])):
                dir2 = dirboard[j][i]
                if dir2 == '_':
                    continue
                hdist = i-x
                dirmoves[dir1+dir2] = []
                if hdist > 0:
                    dirmoves[dir1+dir2].append(['>']*hdist)
                elif hdist < 0:
                    dirmoves[dir1+dir2].append(['<']*abs(hdist))
                vdist = j-y
                if vdist < 0:
                    dirmoves[dir1+dir2].append(['^']*abs(vdist))
                elif vdist > 0:
                    dirmoves[dir1+dir2].append(['v']*abs(vdist))

print("")
print(dirmoves)
# input()

# print(kbmoves)
for d in dirmoves.keys():
    if len(dirmoves[d]) > 1:
        buttons = dirmoves[d]
        newbuttons = []
        dir1 = d[0]
        dir2 = d[1]
        # print(key1,key2,buttons)
        if not(dirplaces[dir1][0] == 0 and dirplaces[dir2][1] == 0):
            newbuttons.append(buttons[1]+buttons[0])
        if not(dirplaces[dir2][0] == 0 and dirplaces[dir1][1] == 0):
            newbuttons.append(buttons[0]+buttons[1])
        # print("now",newbuttons)
        dirmoves[d] = newbuttons.copy()

# print(keyplaces)
# print(dirplaces)

# print(dirmoves)

##############
## PART 1
############
time2 = time.time()
answer = 0
for task in dataset:
    l1options = []
    for x in range(len(task)-1):
        action = task[x:x+2]
        toadd = []
        for a in kbmoves[action]:
            toadd.append("".join(a)+"A")
        l1options.append(toadd)

    # print(l1options)
    # input()
    l1options = ["".join(x) for x in itertools.product(*l1options)]
    # print(l1options)
    # input()

    l2options = []
    for l1option in l1options:
        l1option = "A"+l1option
        l2froml1option = []
        for x in range(len(l1option)-1):
            action = l1option[x:x+2]
            toadd = []
            for a in dirmoves[action]:
                temp = "".join(a)
                temp += "A"
                toadd.append(temp)
            if toadd == []:
                toadd = ["A"]  
            l2froml1option.append(toadd)
        l2froml1option = ["".join(x) for x in itertools.product(*l2froml1option)]
        l2options += l2froml1option

    l3options = []
    for l2option in l2options:
        l2option = "A"+l2option
        l3froml2option = []
        for x in range(len(l2option)-1):
            action = l2option[x:x+2]
            toadd = []
            for a in dirmoves[action]:
                temp = "".join(a)
                temp += "A"
                toadd.append(temp)
            if toadd == []:
                toadd = ["A"]  
            l3froml2option.append(toadd)
        l3froml2option = ["".join(x) for x in itertools.product(*l3froml2option)]
        l3options += l3froml2option

    lengths = []
    for l3o in l3options:
        lengths.append(len(l3o))
    answer+=min(lengths)*int(task[1:4])
    # input()

time3 = time.time()
print("Part 1:",answer)

############
# Part 2
############



# def dorobot(prevoptions):
#     nextoptions = []
#     for option in prevoptions:
#         option = "A"+option
#         newoptions = []
#         for x in range(len(option)-1):
#             action = option[x:x+2]
#             toadd = []
#             for a in dirmoves[action]:
#                 temp = "".join(a)
#                 temp += "A"
#                 toadd.append(temp)
#             if toadd == []:
#                 toadd = ["A"]
#             newoptions.append(toadd)
#         newoptions = ["".join(x) for x in itertools.product(*newoptions)]
#         nextoptions += newoptions
#     return nextoptions.copy()

@functools.cache
def getbestpath(key1,key2,depth):
    if depth == 1:
        #  print("dist is based on",dirmoves[key1+key2])
         return len(dirmoves[key1+key2][0])+1
    beststeps = -1
    for move in dirmoves[key1+key2]:
        steps = 0
        move = ["A"] + move + ["A"]
        # print("Move is ",move)
        for x in range(len(move)-1):
            steps+=getbestpath(move[x],move[x+1],depth-1)
        if beststeps < 0 or steps < beststeps:
            beststeps = steps
    return beststeps

for dirmove in dirmoves:
    if dirmoves[dirmove] == []:
        dirmoves[dirmove] = [[]]

answer = 0
for task in dataset:
    l1options = []
    for x in range(len(task)-1):
        action = task[x:x+2]
        toadd = []
        for a in kbmoves[action]:
            toadd.append("".join(a)+"A")
        l1options.append(toadd)
    l1options = ["".join(x) for x in itertools.product(*l1options)]
    # print(l1options)

    beststeps = -1
    for option in l1options:
        print(option)
        steps = 0
        option = "A"+option
        for x in range(len(option)-1):
            step = getbestpath(option[x:x+1],option[x+1:x+2],25)
            # print(option[x:x+1],option[x+1:x+2],step)
            steps+=step
        if beststeps == -1 or steps < beststeps:
            beststeps = steps
        # print("best steps",beststeps)

    answer+=beststeps*int(task[1:4])


time4 = time.time()
print("Part 2:",answer)


print("Data struct:",time2-time1)
print("Part 1 time:",time3-time2)
print("Part 2 time:",time4-time3)