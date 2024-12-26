import time

with open('24.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

blankline = False
wires = {}
gates = []
for line in dataset:
    if blankline == True:
        gates.append(line)
    elif line == "":
        blankline = True
    else:
        lineparts = line.split(": ")
        wires[lineparts[0]] = int(lineparts[1])

print(gates)
print(wires)

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
    print("doing",gate)
    if gate[0] in wires.keys() and gate[2] in wires.keys():
        wires[gate[4]] = processGate(gate[0],gate[1],gate[2])
        print(gate[4],wires[gate[4]])
    else:
        gates.append(" ".join(gate))
    
output = ""
zkeys = list(wires.keys())
zkeys.sort(reverse=True)
for k in zkeys:
    if k[0:1] == "z":
        print(k,wires[k])
        output+=str(wires[k])
print("Part 1:",int(output,2))
