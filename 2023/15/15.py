with open('15.in') as f:
    data = f.readline()

data = data.split(",")
answer = 0
for x in data:
    runningval = 0
    for n in range(0,len(x)):
        runningval+=ord(x[n])
        runningval*=17
        runningval = runningval%256
        print(runningval)
    answer+=runningval
print("part 1:",answer)