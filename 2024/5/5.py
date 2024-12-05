with open('5.test') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

x = 0
mustBeBefore = {}
mustBeAfter = {}
while dataset[x] != "":
    a,b = dataset[x].split("|")
    if a not in mustBeAfter.keys():
        mustBeAfter[a] = [b]
    else:
        mustBeAfter[a].append(b)
    if b not in mustBeBefore.keys():
        mustBeBefore[b] = [a]
    else:
        mustBeBefore[b].append(a)
    x+=1

print(mustBeAfter)
print(mustBeBefore)

x+=1


totalOfMiddles = 0
while x < len(dataset):
    update = dataset[x].split(",")
    print(update)
    z = len(update)
    badUpdate = False
    for a in range(0,z):
        for b in range(0,z):
            if a < b:
                if update[a] not in mustBeAfter.keys() or update[b] not in mustBeAfter[update[a]]:
                    print(update[b], "not in mustBeAfter",update[a])
                    badUpdate = True
            if a > b:
                if update[a] not in mustBeBefore.keys() or update[b] not in mustBeBefore[update[a]]:
                    print(update[b],"not in mustBeBefore",update[a])
                    badUpdate = True

    if not badUpdate:
        totalOfMiddles+= int(update[int(z/2)])

    x+=1

print("part1",totalOfMiddles)


