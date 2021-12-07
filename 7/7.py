import statistics
crabsubsstr = input().split(',')
crabsubs = [int(i) for i in crabsubsstr]
crabmedian = int(statistics.median(crabsubs))

print(str(crabmedian))

fuel = 0
for x in crabsubs:
    fuel+=abs(x-crabmedian)
print(fuel)