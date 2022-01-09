instructions = []
mainvalue = 0

while True:
    newline = input()
    if newline == '':
        break
    instructions.append([newline,0])

instID = 0
while True:
    inst,count = instructions[instID]
    if count == 1:
        break
    instructions[instID][1]+=1
    if inst[0:3] == 'acc':
        mainvalue += int(inst[4:])
    if inst[0:3] == 'jmp':
        instID+= int(inst[4:])
        continue
    instID+=1

print(mainvalue)

