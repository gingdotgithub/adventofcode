import time
import re
import numpy as math

data = open('24.in').read().splitlines()
starttime = time.time()

hailstones = {}

for row in range(0,len(data)):
    hailstone = tuple(map(int,re.split('[@|,]', data[row])))
    hailstones[row] = hailstone

#print(len(hailstones))
def part1(lowlimit,highlimit):
    answer = 0
    for a in range(0,len(hailstones)):
        for b in range(a+1,len(hailstones)):
            print("doing",hailstones[a],hailstones[b])
            grada = hailstones[a][4] / hailstones[a][3]#((hailstones[a][1]+hailstones[a][4])-hailstones[a][1]) / ((hailstones[a][0]+hailstones[a][3])-hailstones[a][0])
            gradb = hailstones[b][4] / hailstones[b][3]#((hailstones[b][1]+hailstones[b][4])-hailstones[b][1]) / ((hailstones[b][0]+hailstones[b][3])-hailstones[b][0])
            ca = (grada*(-hailstones[a][0])) + hailstones[a][1] 
            cb = (gradb*(-hailstones[b][0])) + hailstones[b][1]
            if grada == gradb: 
                print("they never intserect - parallel")
                print("y = ",grada,"x + ",ca)
                print("y = ",gradb,"x + ",cb)
                continue
            intersectx = -((cb-ca) / (gradb - grada))
            intersecty = -(((cb*grada)-(ca*gradb)) / (gradb-grada))
            if all([math.sign(intersectx-hailstones[a][0]) == math.sign(hailstones[a][3]),
                    math.sign(intersecty-hailstones[a][1]) == math.sign(hailstones[a][4]),
                    math.sign(intersectx-hailstones[b][0]) == math.sign(hailstones[b][3]),
                    math.sign(intersecty-hailstones[b][1]) == math.sign(hailstones[b][4])]):
                if lowlimit <= intersectx <= highlimit and lowlimit <= intersecty <= highlimit:
                    answer+=1
                    print("found intersection at",(intersectx,intersecty))
                else:
                    print("outside of region of interest")
                    if min(abs(intersectx-lowlimit),abs(intersectx-highlimit)) < 10 or min(abs(intersecty-lowlimit),abs(intersecty-highlimit)) < 10:
                        print("dist from x",min(abs(intersectx-lowlimit),abs(intersectx-highlimit)))
                        print("dist from y",min(abs(intersecty-lowlimit),abs(intersecty-highlimit)))
                        f = input("?")
            else:
                print("in someones past")
    return answer

#answer = part1(7,27)
answer = part1(200000000000000,400000000000000)
print("part 1:",answer)
# 26436 = wrong

