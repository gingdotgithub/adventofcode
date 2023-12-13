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
        if area[x] == area[x+1]:
            print("found a possible reflect line")
            dist = min(x+1,len(area)-1-x)
            print("dist to start is",x+1)
            print("dist to end is",len(area)-1-x)
            for i in range(1,dist):
                print(area[x-i])
                print(area[x+1+i])
                if area[x-i] != area[x+1+i]:
                    stillreflect = False
            if stillreflect:
                print("found reflect at:",x)
                hmirrorline = x+1
                answer+=(100*(hmirrorline))
                break
        if stillreflect == False:
            print("no line found")

    #checking across columns for a vertical mirror line 
    if hmirrorline == -1:
        vmirrorline = -1
        print("doing cols:",len(area[0]))
        for x in range(0,len(area[0])-1):
            stillreflect = True
            colM = "".join([line[x] for line in area])
            colN = "".join([line[x+1] for line in area])
            print(colM)
            print(colN)
            if colM == colN:
                print("found a possible reflect vertical at ",x)
                dist=min(x+1,len(area[0])-1-x)
                for i in range(1,dist):
                    colM = "".join([line[x-i] for line in area])
                    colN = "".join([line[x+1+i] for line in area])
                    if colM != colN:
                        stillreflect = False
                if stillreflect:
                    print("found vertical reflect at",x)
                    vmirrorline = x+1
                    answer+=vmirrorline
                    break
            if stillreflect == False:
                print("no vertical found")

print("part 1:", answer)



