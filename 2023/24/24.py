import time
import re
import numpy as np
import sympy

data = open('24.in').read().splitlines()
starttime = time.time()

hailstones = {}

for row in range(0,len(data)):
    hailstone = tuple(map(int,re.split('[@|,]', data[row])))
    hailstones[row] = hailstone

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
                continue
            intersectx = -((cb-ca) / (gradb - grada))
            intersecty = -(((cb*grada)-(ca*gradb)) / (gradb-grada))
            if all([np.sign(intersectx-hailstones[a][0]) == np.sign(hailstones[a][3]),
                    np.sign(intersecty-hailstones[a][1]) == np.sign(hailstones[a][4]),
                    np.sign(intersectx-hailstones[b][0]) == np.sign(hailstones[b][3]),
                    np.sign(intersecty-hailstones[b][1]) == np.sign(hailstones[b][4])]):
                if lowlimit <= intersectx <= highlimit and lowlimit <= intersecty <= highlimit:
                    answer+=1
                    print("found intersection at",(intersectx,intersecty))
                else:
                    print("outside of region of interest")
            else:
                print("in someones past")
    return answer

#answer = part1(7,27)
answer = part1(200000000000000,400000000000000)
endtime = time.time()
print("part 1:",answer)
print("part 1 timing",endtime-starttime)


starttime = time.time()
answer2 = 0
rockx,rocky,rockz,rockvx,rockvy,rockvz = sympy.symbols("rockx,rocky,rockz,rockvx,rockvy,rockyz")
equations = []
for hailstone in hailstones:
    hsx,hsy,hsz,hsvx,hsvy,hsvz = hailstones[hailstone]
    equations.append(((rockx-hsx) * (hsvy-rockvy)) - ((rocky-hsy)*(hsvx-rockvx))) 
    equations.append(((rocky-hsy) * (hsvz-rockvz)) - ((rockz-hsz)*(hsvy-rockvy)))
    #there's a lot here i still dont really understand in terms of the maths. but thank you to HyperNeutrino on youtube. 
    #https://www.youtube.com/watch?v=guOyA7Ijqgk
answer2 = sympy.solve(equations)
print(answer2)
endtime = time.time()
print("part 2:",answer2[0][rockx]+answer2[0][rocky]+answer2[0][rockz])
print("part 2 timing:",endtime-starttime)



