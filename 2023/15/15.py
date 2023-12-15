import re

with open('15.in') as f:
    data = f.readline()

data = data.split(",")
def part1():
    answer = 0
    for x in data:
        answer+=hashit(x)
    print("part 1:",answer)

def hashit(value):
    runningval = 0
    for n in range(0,len(value)):
        runningval+=ord(value[n])
        runningval*=17
        runningval = runningval%256
        #print(runningval)
    return runningval

def part2():
    hashmap = {}
    for x in data:
        if "=" in x:
            hashbit,val = x.split("=")
            symbol = "="
        else:
            hashbit = x[:len(x)-1]
            symbol = "-"
            val=""
        #print(hashbit,symbol,val)
        boxid = hashit(hashbit)
        if boxid not in hashmap.keys():
            hashmap[boxid] = {}
        if symbol in "=":
            #if hashbit not in hashmap[boxid].keys()
            hashmap[boxid][hashbit] = val
        if symbol in "-":
            if hashbit in hashmap[boxid].keys():
                hashmap[boxid].pop(hashbit)
        #print(hashmap)
    answer = 0
    for box in hashmap.keys():
        lenscount = 0
        for lens in hashmap[box].keys():
            lenscount+=1
            answer += ((box+1) * lenscount * int(hashmap[box][lens]))
    print("Part 2:",answer)

part1()
part2()