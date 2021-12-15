readvalues = []
while True:
    newline = input()
    if newline == '':
        break
    readvalues.append(newline)

minvalue = min(readvalues)
sortedvalues = sorted(readvalues)
for x in range(len(sortedvalues)):
    for y in range(x+1,len(sortedvalues)):
        if str(2020-int(sortedvalues[x])-int(sortedvalues[y])) in sortedvalues:
            print(str(int(sortedvalues[x])*int(sortedvalues[y])*(2020-int(sortedvalues[x])-int(sortedvalues[y]))))
            break
