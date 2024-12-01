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

gap = 0
for x in range(len(set1)):
    gap = gap + abs(set1[x]-set2[x])

print(gap)

