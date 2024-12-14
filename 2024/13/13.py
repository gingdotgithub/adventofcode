import time
import re
import numpy as np

time1=time.time()
with open('13.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

costa = 3
costb = 1
costb
machines = []
x=0
while x < len(dataset):
    a = list(map(int,re.findall("\d+",dataset[x])))
    b = list(map(int,re.findall("\d+",dataset[x+1])))
    t = list(map(int,re.findall("\d+",dataset[x+2])))
    machines.append([[[a[0],b[0]],[a[1],b[1]]],[t[0],t[1]]])
    x+=4

# print(machines)

def part1():
    total = 0
    for machine in machines:
        options = list(map(float,np.linalg.inv(machine[0]).dot(machine[1])))
        # options = list(map(float,np.linalg.solve(machine[0],machine[1])))
        # print(options)
        if -0.001 < options[0]-round(options[0]) < 0.001 and -0.001 < options[1]-round(options[1]) < 0.001:
            # print("found one",options)
            total+=(round(options[0])*costa)+(round(options[1])*costb)
        # else:
            # print("not one",options)
    return total
total = part1()    
print("part 1:",total)
time2=time.time()


for machine in machines:
    machine[1][0]+= 10000000000000
    machine[1][1]+= 10000000000000
# print(machines)

total = part1()
print("part 2:",total)
time3=time.time()

print("Part 1 time:",time2-time1)
print("Part 2 time:",time3-time2)
