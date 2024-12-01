with open('1.in') as f:
    dataset = f.readlines()

set1 = []
set2 = []
for row in dataset:
    row = row.split()
    set1.append(int(row[0]))
    set2.append(int(row[1]))

set1.sort()
set2.sort()

print(set1)
print(set2)
print()

#part 1
gap = 0
for x in range(len(set1)):
    gap = gap + abs(set1[x]-set2[x])

print(gap)

#part 2
simlist = {}
for x in range(len(set2)):
    if set2[x] in set1:
        if set2[x] not in simlist.keys():
            simlist[set2[x]] = 0
        simlist[set2[x]] += set2[x]

print(simlist)
gap = 0
for x in range(len(set1)):
    if set1[x] in simlist.keys():
        gap += simlist[set1[x]]
        print("added!")
print(gap)