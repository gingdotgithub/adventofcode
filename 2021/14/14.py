startingcode = input()
#print('start = '+ startingcode[0:2])
reference = {}
counts = {}

input()
while True:
    newline = input()
    if newline == '':
        break
    parts = newline.split(' -> ')
    reference[parts[0]] = parts[1]

for x in range(10):
    newcode = ''
    for y in range(len(startingcode)-1):
        newcode+=startingcode[y:y+1] + reference[startingcode[y:y+2]]
    n = len(startingcode)
    startingcode = newcode + startingcode[n-1:n]
    #print("step " + str(x+1) + ": " + startingcode)

for x in range(len(startingcode)):
    letter = startingcode[x:x+1]
    if letter in counts.keys():
        counts[letter]+=1
    else:
        counts[letter] = 1

print(str(max(counts.values()) - min(counts.values())))

