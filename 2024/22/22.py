import time

with open('22.in') as f:
    dataset = f.readlines()
    dataset = [int(line.rstrip('\n')) for line in dataset]

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

total = 0
for n in dataset:
    answer = n
    for x in range(2000):
        answer = mul64(answer)
        answer = div32(answer)
        answer = mul2048(answer)
    total+=answer
    # print(n,":",answer)
print("Part 1:",total)        