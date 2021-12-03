countof1s = [0]*12
datalength = 0
gamma = ""
epsilon = ""
while True:
    line = input()
    if line == '':
        break
    content = list(line)
    datalength+=1
    for x in range(12):
        countof1s[x]+=int(content[x])
print(countof1s)
for x in range(12):
    if countof1s[x] > datalength/2:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
gammaint = int(gamma,2)
epsilonint = int(epsilon,2)
answer = gammaint*epsilonint
print("answer: " + str(answer))