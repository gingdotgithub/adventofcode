import time
import sys

sys.setrecursionlimit(100000)

time1=time.time()
with open('17.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
    dataset = [line.split(": ") for line in dataset]

registerIDs = "ABC"
registers = []
ops = list(map(int,dataset[4][1].split(",")))
registers.append(int(dataset[0][1]))
registers.append(int(dataset[1][1]))
registers.append(int(dataset[2][1]))
ip = 0
mainoutput = []

print(registers)
print(ops)
time2 = time.time()
def getcombooperand(operand):
    if 3 < operand < 7:
        operand = registers[operand-4]
    return operand

def process(opcode, operand,ip):
    if opcode == 0:
        operand = getcombooperand(operand)
        registers[0] = int(registers[0] / (2**operand))
        return ip+2
    elif opcode == 1:
        registers[1] = registers[1] ^ operand
        return ip+2
    elif opcode == 2:
        registers[1] = getcombooperand(operand) % 8
        return ip+2
    elif opcode == 3:
        if registers[0] != 0:
            return operand
        return ip+2
    elif opcode == 4:
        registers[1] = registers[1] ^ registers [2]
        return ip+2
    elif opcode == 5:
        mainoutput.append(str(getcombooperand(operand) % 8))
        return ip+2
    elif opcode == 6:
        operand = getcombooperand(operand)
        registers[1] = int(registers[0] / (2**operand))
        return ip+2
    elif opcode == 7:
        operand = getcombooperand(operand)
        registers[2] = int(registers[0] / (2**operand))
        return ip+2

def part1(ip):
    while ip < len(ops):
        opcode = ops[ip]
        operand = ops[ip+1]
        # print("doing",opcode,operand,ip)
        ip = process(opcode,operand,ip)
        # print(registers)
        # test = input()

part1(ip)
time3 = time.time()
print("Part 1:",",".join(mainoutput))
print("Part 1 time:",time3-time2)

#opscopy = [str(x) for x in ops]
def part2():
    global mainoutput,todos
    for op in range(len(ops)):
        print("op is",op)
        print("todos are",todos)
        todonext = []
        for todo in todos:
            for x in range(8):
                tryingval = (todo << 3) + x
                print('tryingval',tryingval)
                mainoutput = []
                registers[0] = tryingval
                registers[1] = 0
                registers[2] = 0
                part1(0)
                print("mainoutput is",list(map(int,mainoutput)))
                print("matches?",ops[-op-1:])
                if list(map(int,mainoutput)) == ops[-op-1:]:
                    todonext.append(tryingval)
        todos = todonext
        #test = input()
    return todos.copy()
            

todos = [0]
todos = part2()
print(todos)
print(mainoutput)
print(min(todos))
        

## OLD CODE THAT WILL NEVER END
# val = 10000000
# 
# 
# while mainoutput != opscopy:
#     val+=1
#     # print("trying",val)
#     # print(mainoutput,ops)
#     mainoutput = []
#     registers[0] = val
#     registers[1] = 0
#     registers[2] = 0
#     ip = 0
#     part1(ip)
#     if ",".join(mainoutput).endswith("5,4,1,5,5,0,3,3,0"):
#         print(val,"made",",".join(mainoutput))
#     # test = input()

