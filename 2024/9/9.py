with open('9.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

diskmap = list(dataset[0])

def printdiskmap(diskmap):
    incrID = 0
    output = ""
    for index in range(len(diskmap)):
        if (index & 1) == 0:
            output+=(str(incrID)*int(diskmap[index]))
            incrID+=1
        else:
            output+="."*int(diskmap[index])
        index+=1
    print(output)
    return output

def processdiskmap(diskmap):
    filesystem = []
    gaps = []
    files = []
    incrID = 0
    for index in range(len(diskmap)):
        if (index & 1) == 0:
            files.append([len(filesystem),len(filesystem)+int(diskmap[index])])
            for i in range(int(diskmap[index])):
                filesystem.append(str(incrID))
            incrID+=1
        else:
            gaps.append([len(filesystem),len(filesystem)+int(diskmap[index])])
            for i in range(int(diskmap[index])):
                filesystem.append(".")
        index+=1
        # print(len(filesystem))
    return filesystem, gaps, files

output = printdiskmap(diskmap)
filesystem, gaps, files = processdiskmap(diskmap)

# print(filesystem)
# print(gaps)

def part1(filesystem, gaps):
    i = len(filesystem)
    while len(gaps) > 0 and i > gaps[0][0]:
        if gaps[0][0] == gaps[0][1]:
            gaps.pop(0)
            continue
        i-=1
        if filesystem[i] != ".":
            filesystem[gaps[0][0]] = filesystem[i]
            filesystem[i] = "."
            gaps[0][0] += 1
            # print(filesystem)
            # print(gaps)
        
    # print(filesystem)
    # print(gaps)
    return filesystem, gaps

def part2(filesystem, gaps, files):
    i = len(files)-1
    while i > 0:
        filelen = files[i][1]-files[i][0]
        # print(filelen)
        j = 0
        while j < len(gaps) and gaps[j] < files[i]:
            # if gaps[0][0] == gaps[0][1]:
            #     gaps.pop(0)
            #     continue
            gaplen = gaps[j][1]-gaps[j][0]
            if gaplen >= filelen:
                file = filesystem[files[i][0]:files[i][1]]
                filesystem[gaps[j][0]:gaps[j][0]+len(file)] = file
                filesystem[files[i][0]:files[i][1]] = ["."]*len(file)
                gaps[j][0]+=len(file)
                # print(filesystem)
                # print(gaps)
                break

            j+=1
        i-=1


    return filesystem, gaps, files

def calcchecksum(filesystem):
    inc = 0
    checksum = 0
    for x in filesystem:
        if x != '.':
            # break
            checksum += inc * int(x)
        inc+=1
    return checksum

filesystem, gaps = part1(filesystem,gaps)

print(filesystem)
print("part1:",calcchecksum(filesystem))

filesystem, gaps, files = processdiskmap(diskmap)
print(filesystem)
filesystem, gaps, files = part2(filesystem,gaps,files)
print(filesystem)
print("part2:",calcchecksum(filesystem))

