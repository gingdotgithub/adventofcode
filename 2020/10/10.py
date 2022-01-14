from collections import Counter
jolters = []
distances = Counter()
combinations = Counter()

jolters.append(0)
while True:
    newline = input()
    if newline == '':
        break
    jolters.append(int(newline))
jolters = sorted(jolters)
jolters.append(jolters[len(jolters)-1]+3)
#print(jolters)

def process_combos(x):
    global combinations,jolters
    options = 0
    maxx = len(jolters)-1
    y = 1
    while True:
        if x+y <= maxx:
            if jolters[x+y] - jolters[x] <= 3:
                options = options + combinations[x+y]
            else:
                break
        else:
            break
        y+=1
    return options


for x in range(len(jolters)-1):
    distances[jolters[x+1]-jolters[x]]+=1

#part 1
print(distances[1]*distances[3])

#part 2
x = len(jolters)-2
combinations[len(jolters)-1] = 1
while x >= 0:
    combinations[x] = process_combos(x)
    x-=1
print(combinations[0])