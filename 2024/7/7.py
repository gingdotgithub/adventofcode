import math

def domath(nums,ops):
    operators = ["*","+","||"]
    # print(nums,ops)
    sum=int(nums[0])
    x = 0
    while x < len(ops):
        if ops[x] == '2':
            sum = int(str(sum) + str(nums[x+1]))
            # print(sum)
        else:
            sum = eval(str(sum) + operators[int(ops[x])] + str(nums[x+1]))
        x+=1
    # sum += eval(str(sum) + str(nums[x]))
    # print(sum)
    return sum
        

with open('7.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

maths = {}
for line in dataset:
    total, parts = line.split(": ")
    maths[int(total)] = [int(x) for x in parts.split()]

total = 0
for key in maths.keys():
    maxbinary = "1"*(len(maths[key])-1)
    binarylength = len(maxbinary)
    maxint = int(maxbinary,2)
    for x in range(maxint+1):
        xbinary = "{0:b}".format(x)
        xbinary = ("0"*(binarylength-len(xbinary)))+xbinary
        score = domath(maths[key],xbinary)
        if score == int(key):
            total+=key
            # print("found one!")
            break
    # print("not found")

        
# print(maths)
print("part1:",total,"\n\n")

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

total = 0
for key in maths.keys():
    maxbinary = "2"*(len(maths[key])-1)
    binarylength = len(maxbinary)
    maxint = int(maxbinary,3)
    for x in range(maxint+1):
        xbinary = ternary(x)
        xbinary = ("0"*(binarylength-len(xbinary)))+xbinary
        score = domath(maths[key],xbinary)
        if score == int(key):
            total+=key
            # print("found one!")
            break
    # print("not found")

print("part2", total)