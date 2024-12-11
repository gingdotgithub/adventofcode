import time

time1=time.time()
with open('11.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
time2=time.time()

parts = dataset[0].split(" ")
blinks = 25
for i in range(blinks):
    x = 0
    while x < len(parts):
        if parts[x] == '0':
            parts[x] = '1'
        elif len(parts[x]) & 1 == 0:
            mid = int(len(parts[x])/2)
            parta = str(int(parts[x][:mid]))
            partb = str(int(parts[x][mid:]))
            parts[x] = parta
            parts.insert(x+1,partb)
            x+=1
        else:
            parts[x] = str(int(parts[x])*2024)
        x+=1
    # print(parts)
    # test = input()
    print("doing round",i+1)
    i+=1

print("part1",len(parts))


