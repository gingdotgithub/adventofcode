
with open('14.in') as f:
    data = f.readlines()

for x in range(0,len(data)):
    print(data[x])
    data[x] = list(data[x].strip())
print(data)

def rotate(data):
    data = [list(r) for r in zip(*data[::1])]
    print(data)
    return data

def calcweight(cols):
    answer = 0
    for x in range(0,len(cols)):
        for y in range(0,len(cols[x])):
            if cols[x][y] == "O":
                answer += (len(cols[x])-y)
    return answer


def tilt(cols):
    for x in range(0,len(cols)):
        dots = []
        for y in range(0,len(cols[x])):
            print("checking",x,y,cols[x][y])
            if cols[x][y] == ".":
                dots.append(y)
            elif cols[x][y] == "#":
                dots = []
            elif cols[x][y] == "O":
                if len(dots) > 0:
                    lowestdot = dots.pop(0)
                    cols[x][lowestdot] = "O"
                    cols[x][y] = "."
                    dots.append(y)

    return cols

data = rotate(data)
data = tilt(data)
answer = calcweight(data)
print("part 1:",answer)



# answer = 0
# for n in range(0,2):
#     for m in range(0,4):
#         reversed = False
#         if m > 1:
#             reversed = True
#         answer,data = tilt(data,reversed)
#         for row in data:
#             print(row)

# answer = 0
# cols = []
# for y in range(0,len(data[0])):
#     cols.append([])
# for x in range(0,len(data)):
#     for y in range(0,len(data[x])):
#         cols[y].append(data[x][y])

# for row in cols:
#     print(row)

# print("part 2:",answer)

