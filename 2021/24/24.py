import math

myvs = {'w':0,'x':0,'y':0,'z':0}
instructions = []
zmods = []
mvals = []
nvals = []
inputval = ""

def process_ALU(inst):
    global myvs
    global inputval
    if len(inst) > 2:
        if str(inst[2]).lstrip('-').isnumeric() != True:
            inst[2] = myvs[inst[2]]
        else:
            inst[2] = int(inst[2])
    if inst[0] == 'inp':
        myvs[inst[1]] = int(inputval[0:1])
        inputval = inputval[1:]
    elif inst[0] == 'add':
        myvs[inst[1]]+=inst[2]
    elif inst[0] == 'mul':
        myvs[inst[1]]*=inst[2]
    elif inst[0] == 'div' and inst[2] != 0:
        myvs[inst[1]] = myvs[inst[1]] // inst[2]
    elif inst[0] == 'mod' and myvs[inst[1]] >= 0 and inst[2] > 0:
        myvs[inst[1]] = myvs[inst[1]] % inst[2]
    elif inst[0] == 'eql':
        myvs[inst[1]] = 1 if myvs[inst[1]] == inst[2] else 0
    return myvs['z']


while True:
    newline = input()
    if newline == "":
        break
    if newline == 'div z 1':
        zmods.append(1)
    if newline == 'div z 26':
        zmods.append(0)
    if newline[0:5] == 'add x' and newline[-1:] != 'z':
        mvals.append(int(newline[6:]))
    if newline[0:5] == 'add y' and newline[6:] not in ['25','1','w']:
        nvals.append(int(newline[6:]))
    instructions.append(newline.split())


inputnum = 10000000
answer = 1
while answer > 0:
    inputnum-=1
    inputval = ""
    mystack = []
    inputs = list(str(inputnum))
    myzmods = zmods.copy()
    mymvals = mvals.copy()
    mynvals = nvals.copy()
    for z in myzmods:
        if z == 1:
            temp = int(inputs.pop(0))
            inputval+=str(temp)
            mystack.append(temp+mynvals.pop(0))
            mymvals.pop(0)
        else:
            temp = mystack.pop()+mymvals.pop(0)
            if temp > 9 or temp < 1:
                break
            mynvals.pop(0)
            inputval+=str(temp)
    if len(inputval) == 14:
        print("trying" + inputval)
        instcopy = instructions.copy()
        result = 0
        for inst in instcopy:
            #if inst[0] == 'inp':
            #    print("w="+str(myvs['w'])+",x="+str(myvs['x'])+",y="+str(myvs['y'])+",z="+str(myvs['z']))
            result = process_ALU(inst)
        answer = result
    else:
        answer = 1
print(answer)
print(inputval)