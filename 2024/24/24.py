import time

with open('24.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

blankline = False
wires = {}
gates = []
gatesdict = {}
for line in dataset:
    if blankline == True:
        gates.append(line)
        linedata = line.split(" ")
        gatesdict[linedata[4]] = (linedata[1],linedata[0],linedata[2])
    elif line == "":
        blankline = True
    else:
        lineparts = line.split(": ")
        wires[lineparts[0]] = int(lineparts[1])

# print(gates)
# print(wires)
time1 = time.time()

def processGate(val1, op, val2):
    val1 = wires[val1]
    val2 = wires[val2]
    if op == "AND":
        if val1 == 1 and val2 == 1:
            return 1
        else:
            return 0
    elif op == "OR":
        if val1 == 1 or val2 == 1:
            return 1
        else:
            return 0
    elif op == "XOR":
        if val1 != val2:
            return 1
        else:
            return 0

while len(gates) > 0:
    gate = gates.pop(0).split(" ")
    # print("doing",gate)
    if gate[0] in wires.keys() and gate[2] in wires.keys():
        wires[gate[4]] = processGate(gate[0],gate[1],gate[2])
        # print(gate[4],wires[gate[4]])
    else:
        gates.append(" ".join(gate))
    
output = ""
zkeys = list(wires.keys())
zkeys.sort(reverse=True)
for k in zkeys:
    if k[0:1] == "z":
        # print(k,wires[k])
        output+=str(wires[k])
print("Part 1:",int(output,2))
time2 = time.time()

###########
#Part 2
#with thanks to learning from https://www.youtube.com/watch?v=SU6lp6wyd3I 
###########

def vizboard(wire,depth=0):
    if wire[0] == 'x' or wire[0] == 'y':
        return (" -> "*depth) + wire
    g,a,b = gatesdict[wire]
    return (" -> "*depth) + g + " (" + wire + ")\n" + vizboard(a,depth+1) + "\n" + vizboard(b,depth+1)
# print(gatesdict)
print(vizboard("z15"))

def genwire(char,num):
    return char + str(num).rjust(2,"0")

def verify_z(wire,num):
    print("vz",wire,num)
    if wire not in gatesdict:
        return False
    g,x,y = gatesdict[wire]
    if g != 'XOR':
        return False
    if num == 0:
        return sorted([x,y]) == ["x00","y00"]
    return verify_intermediate_xor(x,num) and verify_carry_bit(y,num) or verify_intermediate_xor(y,num) and verify_carry_bit(x,num)

def verify_intermediate_xor(wire,num):
    print("vx",wire,num)
    if wire not in gatesdict:
        return False
    g,x,y = gatesdict[wire]
    if g != 'XOR':
        return False
    return sorted([x,y]) == [genwire("x",num),genwire("y",num)]

def verify_carry_bit(wire,num):
    print("vc",wire,num)
    if wire not in gatesdict:
        return False
    g,x,y = gatesdict[wire]
    if num == 1:
        if g != "AND":
            return False
        return sorted([x,y]) == ["x00","y00"]
    if g != "OR":
        return False
    return verify_direct_carry(x,num-1) and verify_recarry(y,num-1) or verify_direct_carry(y,num-1) and verify_recarry(x,num-1)

def verify_direct_carry(wire,num):
    print("wd",wire,num)
    if wire not in gatesdict:
        return False
    g,x,y = gatesdict[wire]
    if g != "AND":
        return False
    return sorted([x,y]) == [genwire("x",num),genwire("y",num)]

def verify_recarry(wire,num):
    print("vr",wire,num)
    if wire not in gatesdict:
        return False
    g,x,y = gatesdict[wire]
    if g != "AND":
        return False
    return verify_intermediate_xor(x,num) and verify_carry_bit(y,num) or verify_intermediate_xor(y,num) and verify_carry_bit(x,num)

def verify(num):
    return verify_z(genwire("z",num),num)

def checkforswaps():
    x = 0
    while True:
        if not verify(x):
            break
        x+=1
    return x

swaps = []
for i in range(4):
    sofar = checkforswaps()
    for x in gatesdict:
        for y in gatesdict:
            if x == y:
                continue
            gatesdict[x],gatesdict[y] = gatesdict[y],gatesdict[x]
            if checkforswaps() > sofar:
                break
            gatesdict[x],gatesdict[y] = gatesdict[y],gatesdict[x]
        else:
            continue
        break
    swaps+=[x,y]

print("Part 2:",",".join(sorted(swaps)))
time3 = time.time()

print("Part 1 time:",time2-time1)
print("Part 2 time:",time3-time2)