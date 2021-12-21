skimap = []
angles = [3,1]
pos = [0,0]
hits = 0

while True:
    newline = input()
    if newline == '':
        break
    skimap.append(list(newline))

while pos[1] < len(skimap)-1:
    pos[0] += angles[0]
    pos[1] += angles[1]
    if skimap[pos[1]][pos[0]%len(skimap[0])] == "#":
        hits+=1
    
for row in skimap:
    print("".join(row))
print(hits)