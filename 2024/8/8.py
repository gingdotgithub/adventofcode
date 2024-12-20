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

nodes = []
for key in antns.keys():
    for ant in antns[key]:
        for ant2 in antns[key]:
            print("comparing",ant,"and",ant2)
            if ant != ant2:
                xstart = ant[0]
                ystart = ant[1]
                xdiff = ant2[0]-ant[0]
                ydiff = ant2[1]-ant[1]
                inbox = True
                while inbox:
                    xstart+=xdiff
                    ystart+=ydiff
                    if 0 <= xstart < w and 0 <= ystart < h:
                        if (xstart,ystart) not in nodes:
                            nodes.append((xstart,ystart))
                    else:
                        inbox = False
print(nodes)
nodes = sorted(nodes, key=lambda tup: (tup[0],tup[1]))
print(nodes)
print("part 2:",len(nodes))
