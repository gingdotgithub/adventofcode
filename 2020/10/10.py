from collections import Counter
jolters = []
distances = Counter()

while True:
    newline = input()
    if newline == '':
        break
    jolters.append(int(newline))

jolters = sorted(jolters)

print(jolters)
distances[jolters[0]-0]+=1
for x in range(len(jolters)-1):
    distances[jolters[x+1]-jolters[x]]+=1
distances[3]+=1

print(distances)
print(distances[1]*distances[3])