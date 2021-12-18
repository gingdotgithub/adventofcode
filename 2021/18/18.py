import json
import math

def checkneedsreducing(currentsf):
    anylist = list(range(10,99))
    depth = 0
    literalfound = 0
    stringversion = str(currentsf)
    depthindexfound = len(stringversion)
    literalindexfound = depthindexfound
    for x in range(len(stringversion)):
        if stringversion[x] == "[":
            depth+=1
        if stringversion[x] == "]":
            depth-=1
        if depth == 5:
            depthindexfound = x
            return 1, depthindexfound
    for item in anylist:
        if str(item) in stringversion:
            foundindex = stringversion.index(str(item))
            if foundindex < literalindexfound:
                literalindexfound = foundindex
    if literalindexfound < len(stringversion):
        return 2, literalindexfound
    return 0, 0

def splitliteral(currentsf, indexsf):
    stringversion = str(currentsf)
    left = stringversion[0:indexsf]
    if stringversion[indexsf+2:indexsf+3].isdigit():
        literalstrlen = 3
    else:    
        literalstrlen = 2
    literalstr = stringversion[indexsf:indexsf+literalstrlen]
    newstr = "[" + str(math.floor(int(literalstr)/2)) + "," + str(math.ceil(int(literalstr)/2)) + "]"
    right = stringversion[indexsf+literalstrlen:]
    return json.loads(left+newstr+right)

def explodepair(currentsf,indexsf):
    stringversion = str(currentsf)
    left = stringversion[0:indexsf]
    nextbracket = stringversion.index("]",indexsf)
    (pair0,pair1) = stringversion[indexsf+1:nextbracket].split(", ")
    right = stringversion[nextbracket+1:]
    x = len(left)-1
    while x > 0:
        if (left[x-1:x+1]).isdigit():
            digit = int(left[x-1:x+1])+int(pair0)
            left = left[0:x-1] + str(digit) + left[x+1:]
            break
        if (left[x:x+1]).isdigit():
            digit = int(left[x:x+1])+int(pair0)
            left = left[0:x] + str(digit) + left[x+1:]
            break
        x-=1
    x = 0
    while x < len(right)-2:
        if (right[x:x+2]).isdigit():
            digit = int(right[x:x+2])+int(pair1)
            right = right[0:x] + str(digit) + right[x+2:]
            break
        if (right[x:x+1]).isdigit():
            digit = int(right[x:x+1])+int(pair1)
            right = right[0:x] + str(digit) + right[x+1:]
            break
        x+=1
    return json.loads(left+"0"+right)

def calc_magnitude(mylist):
    total = 0 
    part1 = 0
    part2 = 0
    if isinstance(mylist[0],int):
        part1 = mylist[0]
    else:
        part1 = calc_magnitude(mylist[0])
    if isinstance(mylist[1],int):
        part2 = mylist[1]
    else:
        part2 = calc_magnitude(mylist[1])
    return (3*part1) + (2*part2)

snailfish = []
while True:
    newline = input()
    if newline == '':
        break
    snailfish.append(json.loads(newline))

# ongoingsum = snailfish.pop(0)
# for sf in snailfish:
maxmagnitude = 0
for x in range(len(snailfish)):
    for y in range(len(snailfish)):
        if x != y:
            ongoingsum = [snailfish[x],snailfish[y]]
            needsreducing, indexoffound = checkneedsreducing(ongoingsum)
            while needsreducing > 0:
                print("needs reducing  - " + str(ongoingsum))
                if needsreducing == 1:
                    print("doing depth")
                    ongoingsum = explodepair(ongoingsum, indexoffound)
                elif needsreducing == 2:
                    print("doing literal")
                    ongoingsum = splitliteral(ongoingsum, indexoffound)
                needsreducing, indexoffound = checkneedsreducing(ongoingsum)
            thismagnitude = calc_magnitude(ongoingsum)
            if thismagnitude > maxmagnitude:
                maxmagnitude = thismagnitude
#print("final answer: " + str(ongoingsum)) 
print(int(maxmagnitude))


# test = json.loads("[[[[1,1],[2,2]],[3,3]],[4,4]]")
# answer = calc_magnitude(test)
# answer = json.loads("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
# print(test)
# print(answer)

