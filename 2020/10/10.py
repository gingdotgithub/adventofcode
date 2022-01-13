from collections import Counter
jolters = []
distances = Counter()

jolters.append(0)
while True:
    newline = input()
    if newline == '':
        break
    jolters.append(int(newline))
jolters = sorted(jolters)
jolters.append(jolters[len(jolters)-1]+3)
#print(jolters)

for x in range(len(jolters)-1):
    distances[jolters[x+1]-jolters[x]]+=1

print(distances[1]*distances[3])