import math

skimap = []
angles = [[1,1],[3,1],[5,1],[7,1],[1,2]]
pos = [0,0]
hits = []

while True:
    newline = input()
    if newline == '':
        break
    skimap.append(list(newline))

for angle in angles:
    hit = 0
    pos = [0,0]
    while pos[1] < len(skimap)-1:
        pos[0] += angle[0]
        pos[1] += angle[1]
        if skimap[pos[1]][pos[0]%len(skimap[0])] == "#":
            hit+=1
    hits.append(hit)
    
for row in skimap:
    print("".join(row))
print(str(hits))
print(str(math.prod(hits)))