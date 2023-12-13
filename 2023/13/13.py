with open('13.in') as f:
    allareas = f.readlines()

areas = [[]]
areacount = 0
for x in range(0,len(allareas)):
    line = allareas[x].strip()
    if line == "":
        areacount+=1
        areas.append([])
    else:
        areas[areacount].append(line)

answer = 0
for a in range(0,len(areas)):
    area = areas[a]
    print("Doing Area:",a)
    print("-------------")
    #checking down the rows for a horizontal mirror line 
    hmirrorline = -1
    print("doing rows:",len(area))
    for x in range(0,len(area)-1):
        stillreflect = True
        smudgecount = 0 #this is for part 2 - it should be exactly 1 by the end of a match, or its not the match
        diff = sum(1 for y,z in zip(area[x],area[x+1]) if y!=z) #part 2 this means i can tell if a line is 
        #if area[x] == area[x+1]: #part 2 is replaced below, allowing for smudgecount
        if diff+smudgecount == 1 or diff+smudgecount == 0:
            smudgecount+=diff #this could be 1 or 0 really, but it lets us know whether we've included a smudge yet or not to make the initial match
            print("found a possible reflect line")
            dist = min(x+1,len(area)-1-x)
            print("dist to start is",x+1)
            print("dist to end is",len(area)-1-x)
            for i in range(1,dist):
                print(area[x-i])
                print(area[x+1+i])
                diff = sum(1 for y,z in zip(area[x-i],area[x+1+i]) if y!=z) #part 2 using a smudge number again
                #if area[x-i] != area[x+1+i]:
                if diff+smudgecount > 1: #P2 if we've had to use more than 1 smudge to get here, its not good.
                    stillreflect = False
                else:
                    smudgecount += diff #P2 adding to the smudge count (will be 0 or 1) to check how many smudges we've used
            if stillreflect and smudgecount == 1: #p2 - because smudgecount has to be exactly 1 - this means a natural reflection with no smudge is not allowed
                print("found reflect at:",x)
                hmirrorline = x+1
                answer+=(100*(hmirrorline))
                break
        if stillreflect == False:
            print("no line found")

    #checking across columns for a vertical mirror line 
    #part 2 does the same below as in the horizontal line check above. 
    if hmirrorline == -1:
        vmirrorline = -1
        print("doing cols:",len(area[0]))
        for x in range(0,len(area[0])-1):
            stillreflect = True
            smudgecount = 0
            colM = "".join([line[x] for line in area]) #this is extracting the xth char of each line and making a single string out of it, to treat the same way as the horizontal check
            colN = "".join([line[x+1] for line in area])
            print(colM)
            print(colN)
            diff = sum(1 for y,z in zip(colM,colN) if y!=z)
            if diff+smudgecount == 1 or diff+smudgecount == 0:
                smudgecount+=diff
                print("found a possible reflect vertical at ",x)
                dist=min(x+1,len(area[0])-1-x)
                for i in range(1,dist):
                    colM = "".join([line[x-i] for line in area])
                    colN = "".join([line[x+1+i] for line in area])
                    diff = sum(1 for y,z in zip(colM,colN) if y!=z)
                    #if colM != colN:
                    if diff+smudgecount > 1:
                        stillreflect = False
                    else:
                        smudgecount += diff
                if stillreflect and smudgecount == 1:
                    print("found vertical reflect at",x)
                    vmirrorline = x+1
                    answer+=vmirrorline
                    break
            if stillreflect == False:
                print("no vertical found")

print("part 2:", answer)



