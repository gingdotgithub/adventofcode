no1 = int(input())
no2 = int(input())
no3 = int(input())
no4 = 0
mycount = 0
while True:
    line = input()
    if line == '':
        break
    no4 = int(line)
    if no2+no3+no4 > no1+no2+no3:
        mycount += 1
    no1, no2, no3 = no2, no3, no4
print("output: " + str(mycount))
