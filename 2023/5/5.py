seeds = []
maps = {}

with open('5.test') as f:
    data = f.readlines()
    
seedsdata = data[0].split(":")
seeds = list(map(int, seedsdata[1].split()))
print(seeds)
currmap = ""
for line in range (1,len(data)):
    if data[line] == "\n":
        currmap = data[line+1].split()[0]
        maps[currmap] = {}
        
    elif "map" not in data[line]:
        mapdata = list(map(int,data[line].split()))
        #maps[currmap][range(mapdata[1],mapdata[1]+mapdata[2])] = range(mapdata[0],mapdata[0]+mapdata[2])
        maps[currmap][range(mapdata[1],mapdata[1]+mapdata[2])] = mapdata[0]-mapdata[1]
        
print(maps)
    
lowest = -1
for seed in seeds:
    for mapping in maps:
        #print(mapping)
        for maprange in maps[mapping].keys():
            if seed in maprange:
                seed += maps[mapping][maprange]
                break
        print(mapping,seed)
    if lowest == -1:
        lowest = seed
    elif seed < lowest:
        lowest = seed

print(lowest)
    
