with open('8.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

antns = {}

h=len(dataset)
w=len(dataset[0])
for y in range(h):
    for x in range(w):
        char = dataset[y][x]
        if char not in [".","#"]:
            if char not in antns.keys():
                antns[char] = []
            antns[char].append((x,y))

print(antns)
nodes = []
for key in antns.keys():
    for ant in antns[key]:
        for ant2 in antns[key]:
            print("comparing",ant,"and",ant2)
            if ant != ant2:
                nodex = ant[0]+((ant2[0]-ant[0])*2)
                nodey = ant[1]+((ant2[1]-ant[1])*2)
                print("checking",nodex,nodey)
                if 0 <= nodex < w and 0<= nodey < h and (nodex,nodey) not in nodes:
                    nodes.append((nodex,nodey))
                    print("adding",nodex,nodey)

print("part 1:",len(nodes))


