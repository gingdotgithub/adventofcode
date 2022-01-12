numbers = []
preamble = 25
target = 1639024365

def has_a_sum():
    global numbers, preamble
    for i in range(0,preamble):
        for j in range (i,preamble):
            if numbers[i]+numbers[j] == numbers[preamble]:
                return True
    return False

while True:
    newline = input()
    if newline == '':
        break
    newnum = int(newline)
    numbers.append(newnum)

#while True:
    #if not has_a_sum():
    #    break
    #numbers.pop(0)

#print(numbers[preamble])

for x in range(len(numbers)):
    currentsum = numbers[x]
    currentmin = currentsum
    currentmax = currentsum
    for y in range(x+1,len(numbers)):
        currentsum+=numbers[y]
        if currentsum == target:
            print(currentmin+currentmax)
        elif currentsum > target:
            continue
        elif numbers[y] > currentmax:
            currentmax = numbers[y]
        elif numbers[y] < currentmin:
            currentmin = numbers[y]
        
