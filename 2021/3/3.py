datasize=12
dataset = []
originalcountof1s, countof1s = 0, 0

def myfilter(dataset, position, value):
    filtereddata = []
    nextcountof1s = 0
    if len(dataset) > 1:
        for row in dataset:
            if row[position] == value:
                filtereddata.append(row)
                if position < datasize-1:
                    nextcountof1s+=int(row[position+1])
                else: 
                    nextcountof1s = -1
    else:
        nextcountof1s = -1
        filtereddata = dataset
    return filtereddata, nextcountof1s

while True:
    line = input()
    if line == '':
        break
    content = list(line)
    dataset.append(content)
    originalcountof1s += int(content[0])

print(dataset)
oxydata = dataset
co2data = dataset

countof1s = originalcountof1s
for x in range(datasize):
    print(str(countof1s) + " - " + str(len(oxydata)/2))
    if countof1s >= len(oxydata)/2:
        oxydata, countof1s = myfilter(oxydata,x,"1")
    else:
        oxydata, countof1s = myfilter(oxydata,x,"0")
    print(oxydata)
    if countof1s == -1:
        break

countof1s = originalcountof1s
for x in range(datasize):
    print(str(countof1s) + " - " + str(len(co2data)/2))
    if countof1s >= len(co2data)/2:
        co2data, countof1s = myfilter(co2data,x,"0")
    else:
        co2data, countof1s = myfilter(co2data,x,"1")
    print(co2data)
    if countof1s == -1:
        break

oxyint = int(''.join(oxydata[0]),2)
co2int = int(''.join(co2data[0]),2)
answer = oxyint*co2int
print("answer: " + str(answer))


