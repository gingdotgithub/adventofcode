import copy

instructions = []
mainvalue = 0

while True:
    newline = input()
    if newline == '':
        break
    instructions.append([newline,0])

def process_commands(instructs,target):
    global mainvalue
    mainvalue = 0
    maxinstID = 0
    instID = 0
    while True:
        if instID >= len(instructs):
            return True
        if instID > maxinstID:
            maxinstID = instID
        inst,count = instructs[instID]
        if count == target:
            print(str(maxinstID)+" "+instructs[maxinstID][0])
            break
        instructs[instID][1]+=1
        if inst[0:3] == 'acc':
            mainvalue += int(inst[4:])
        if inst[0:3] == 'jmp':
            instID+= int(inst[4:])
            continue
        instID+=1
    return False

#process_commands(instructions,1)
x = 0
while True:
    alteredinstructions = copy.deepcopy(instructions)
    if alteredinstructions[x][0][0:3] == 'nop':
        alteredinstructions[x][0] = 'jmp' + alteredinstructions[x][0][3:]
    elif alteredinstructions[x][0][0:3] == 'jmp':
        alteredinstructions[x][0] = 'nop' + alteredinstructions[x][0][3:]
    if process_commands(alteredinstructions,1):
        break
    x+=1


print(mainvalue)
