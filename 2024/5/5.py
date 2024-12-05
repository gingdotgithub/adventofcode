with open('5.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

# Reading in rules
x = 0
mustBeBefore = {}
mustBeAfter = {}
while dataset[x] != "":
    a,b = dataset[x].split("|")
    if a not in mustBeAfter.keys():
        mustBeAfter[a] = [b]
    else:
        mustBeAfter[a].append(b)
    x+=1

print(mustBeAfter)

x+=1

# doing Part 1 and Part 2
totalOfMiddles = 0
totalOfBadMiddles = 0
while x < len(dataset):
    update = dataset[x].split(",")
    print(update)
    z = len(update)
    badUpdate = False
    toSwap = False
    a = 0
    while a < z:
        b = a+1
        while b < z:
            if a < b:
                if update[a] not in mustBeAfter.keys() or update[b] not in mustBeAfter[update[a]]:
                    print(update[b], "not in mustBeAfter",update[a])
                    badUpdate = True
                    toSwap = True
            if toSwap: #for badupdates, toswap swaps them and starts the validation again
                print("swapping....")
                print(update)
                update[a], update[b] = update[b], update[a]
                a = 0
                b = 0
                print(update)
                toSwap = False
            b+=1
        a+=1

    if not badUpdate:
        totalOfMiddles+= int(update[int(z/2)])
    else:
        totalOfBadMiddles+= int(update[int(z/2)])

    x+=1

# printing out the answer
print("part1",totalOfMiddles)
print("part2", totalOfBadMiddles)


