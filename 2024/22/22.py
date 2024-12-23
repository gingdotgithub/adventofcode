import time

nth = 2000
with open('22.in') as f:
    dataset = f.readlines()
    dataset = [int(line.rstrip('\n')) for line in dataset]

lastdigits = {}

def mul64(sn):
    sn2 = (sn*64)
    sn = sn2 ^ sn
    sn = sn % 16777216
    return sn

def div32(sn):
    sn2 = int(sn / 32)
    sn = sn2 ^ sn
    sn = sn % 16777216
    return sn

def mul2048(sn):
    sn2 = (sn*2048) 
    sn = sn2 ^ sn
    sn = sn % 16777216
    return sn

def part1():
    total = 0
    for n in dataset:
        lastdigits[n] = [int(str(n)[-1:])]
        answer = n
        for x in range(nth):
            answer = mul64(answer)
            answer = div32(answer)
            answer = mul2048(answer)
            lastdigits[n].append(int(str(answer)[-1:]))
        total+=answer
    return total
        # print(n,":",answer)

time1 = time.time()
total = part1()
time2 = time.time()
print("Part 1:",total)
# print(lastdigits)

def getsum(magicnums):
    total = 0
    # print(magicnums)
    for mn in magicnums:
        total+=magicnums[mn]
    return total

def part2():
    diffs = {}
    pointers = {}
    for n in dataset:
        diffs[n] = []
        for ld in range(1,len(lastdigits[n])):
            diffs[n].append(lastdigits[n][ld]-lastdigits[n][ld-1])
            if ld > 2:
                pointer = str(diffs[n][ld-4:ld])
                if pointer not in pointers:
                    pointers[pointer] = {}
                if n not in pointers[pointer]:
                    # pointers[pointer][n] = []
                    pointers[pointer][n] = lastdigits[n][ld]

    # print(diffs)
    bestsofar = 0
    for point in pointers:
        if len(pointers[point]) > 10:
            # print(point,pointers[point])
            thesum = getsum(pointers[point])
            if thesum > bestsofar:
                bestsofar = thesum
    return bestsofar

        

answer = part2()     
time3 = time.time()  
print("Part 2:",answer)
print("Part 1 time:",time2-time1)
print("Part 2 time:",time3-time2)