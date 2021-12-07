import statistics
import math

def calcfuel(n):
    for i in range(n):
        n+= i
    return n

crabsubsstr = input().split(',')
crabsubs = [int(i) for i in crabsubsstr]
crabmean = int(math.floor(statistics.mean(crabsubs)))

print(str(crabmean))

fuel = 0
for x in crabsubs:
    fuel+=calcfuel(abs(x-crabmean))
print(fuel)