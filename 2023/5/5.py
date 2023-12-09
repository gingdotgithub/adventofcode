import time

seeds = {}
maps = {}

with open('5.in') as f:
    data = f.readlines()
starttime = time.time()


seedsdata = data[0].split(":")
seedranges = list(map(int, seedsdata[1].split()))
#part 2 for seeds
startrange = True
for x in range(0,len(seedranges)):
    if startrange:
        seeds[(seedranges[x],seedranges[x]+seedranges[x+1])] = 0
        startrange = False
    else:
        startrange = True


print(seeds)
currmap = ""
for line in range(1,len(data)):
    if data[line] == "\n":
        currmap = data[line+1].split()[0]
        maps[currmap] = {}
        
    elif "map" not in data[line]:
        mapdata = list(map(int,data[line].split()))
        #maps[currmap][range(mapdata[1],mapdata[1]+mapdata[2])] = range(mapdata[0],mapdata[0]+mapdata[2])
        maps[currmap][(mapdata[1],mapdata[1]+mapdata[2])] = mapdata[0]-mapdata[1]
        
print(maps)

##### was part 1
# lowest = -1
# print(seeds)
# for seed in seeds:
#     print("yes")
#     for mapping in maps:
#         #print(mapping)
#         for maprange in maps[mapping].keys():
#             if seed in maprange:
#                 seed += maps[mapping][maprange]
#                 break
#         print(mapping,seed)
#     if lowest == -1:
#         lowest = seed
#     elif seed < lowest:
#         lowest = seed



for mapping in maps:
    print("doing",mapping)
    for maprange in maps[mapping]:
        newseeds = seeds.copy()
        for seedrange in seeds:
            if seeds[seedrange] == 0:
                if (max(maprange) < min(seedrange)) or (min(maprange) > max(seedrange)):
                    print("not overlapping", seedrange, maprange)
                elif (min(maprange) <= min(seedrange)) and (max(maprange) >= max(seedrange)):
                    #newseeds[seedrange] += maps[mapping][maprange]
                    newrange = (min(seedrange)+maps[mapping][maprange],max(seedrange)+maps[mapping][maprange])
                    print("found a covering span", seedrange, maprange)
                    print(seedrange,"now", newrange)
                    newseeds.pop(seedrange)
                    newseeds[newrange] = 1
                else:
                    seedrangevalue = newseeds.pop(seedrange)
                    change = maps[mapping][maprange]
                    if (min(maprange) < min(seedrange)):
                        leftrange = (min(seedrange)+change,max(maprange)+change)
                        newseeds[leftrange] = 1
                        rightrange = (max(maprange),max(seedrange))
                        newseeds[rightrange] = 0
                        print("found left overlap", seedrange, maprange)
                        print(seedrange,"now",leftrange,"and",rightrange)
                        #print(leftrange,"now",newseeds[leftrange],". ",rightrange,"still",newseeds[rightrange])
                    elif (max(maprange) > max(seedrange)):
                        leftrange = (min(seedrange),min(maprange))
                        newseeds[leftrange] = 0
                        rightrange = (min(maprange)+change,max(seedrange)+change)
                        newseeds[rightrange] = 1
                        print("found right overlap", seedrange, maprange)
                        print(leftrange, rightrange)
                        #print(leftrange,"still",newseeds[leftrange],". ",rightrange,"now",newseeds[rightrange])
                        print(seedrange,"now",leftrange,"and",rightrange)
                    else:
                        leftrange = (min(seedrange),min(maprange))
                        newseeds[leftrange] = 0
                        midrange = (min(maprange)+change,max(maprange)+change)
                        newseeds[midrange] = 1#seedrangevalue + maps[mapping][maprange]
                        rightrange = (max(maprange),max(seedrange))
                        newseeds[rightrange] = 0
                        print("found one entirely inside",seedrange,maprange)
                        print(seedrange,"now",leftrange, midrange, rightrange)
                        #print(leftrange,"still",newseeds[leftrange],". ",midrange,"now",newseeds[midrange],". ",rightrange,"still",newseeds[rightrange])
        seeds = newseeds.copy()
    print("seeds now",seeds)
    for seedrange in seeds:
        seeds[seedrange] = 0

lowest = -1
for seedrange in seeds:
    print(seedrange,lowest)
    if lowest < 0:
        lowest = min(seedrange)
    else:
        if len(seedrange) > 0:
            if min(seedrange) < lowest:
                lowest = min(seedrange)

print("part 2:",lowest)
print("timing: ", time.time()-starttime)
