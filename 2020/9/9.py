numbers = []
preamble = 25

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

while True:
    if not has_a_sum():
        break
    numbers.pop(0)

print(numbers[preamble])
        
