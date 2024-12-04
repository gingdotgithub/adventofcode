
def checkpos(pos):
    (y,x) = pos
    print("checking",y," ",x)
    count = 0
    checks = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for (a,b) in checks:
        print("checking",b,a)
        if (y+(b*3)) >= 0 and (y+(b*3)) < len(dataset) and (x+(a*3)) >= 0 and (x+(a*3)) < len(dataset[0]):
            if dataset[y+(b*1)][x+(a*1)] == 'M' and dataset[y+(b*2)][x+(a*2)] == 'A' and dataset[y+(b*3)][x+(a*3)] == 'S':
                print("found",b,a)
                count+=1
    return count
    

with open('4.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
    print(dataset)

total = 0
for y in range(len(dataset)):
    # print(dataset[y])
    for x in range(len(dataset[0])):
        # print(dataset[y][x])
        if dataset[y][x] == 'X':
            total+=checkpos((y,x))

print("found ",total)
            