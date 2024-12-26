import time

with open('25.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

keys = []
locks = []
row = 0
tempstore = []
islock = False
for line in range(len(dataset)):
    # print('doing line',line,dataset[line])
    if dataset[line] == "":
        # print("found blank line")
        tempstore = list(map(list, zip(*tempstore)))
        if islock:
            locks.append(tempstore.copy())
        else:
            keys.append(tempstore.copy())
        tempstore = []
        islock = False
    else:
        # print("tempstore",tempstore)
        if len(tempstore) == 0 and dataset[line][0] == '#':
            islock = True
        tempstore.append(dataset[line])
tempstore = list(map(list, zip(*tempstore)))
if islock:
    locks.append(tempstore.copy())
else:
    keys.append(tempstore.copy())

lockdata = []
keydata = []
for lock in locks:
    data = []
    for column in lock:
        data.append(column.count('#')-1)
    lockdata.append(data.copy())
for key in keys:
    data = []
    for column in key:
        data.append(column.count('#')-1)
    keydata.append(data.copy())

print(lockdata)
print(keydata)


countfits = 0
for lock in lockdata:
    for key in keydata:
        fits = True
        for x in range(len(key)):
            # print(lock[x])
            if lock[x] + key[x] >= 6:
                fits = False
        if fits:
            countfits+=1

print("Part 1:",countfits)