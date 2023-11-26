import math

def calculate(datatouse):
    asteroids = {}
    with open(datatouse) as f:
        adata = f.readlines()

    for y in range(0,len(adata)):
        line = adata[y].strip()
        for x in range(0,len(line)):
            if line[x] == "#":
                asteroids[(x,y)] = 0

    bestsite = (-1,-1)
    bestsitecount = -1
    for source in asteroids.keys():
        angles = []
        for asteroid in asteroids.keys():
            if asteroid != source:
                angle = math.atan2(asteroid[0]-source[0],asteroid[1]-source[1])
                #print(angle)
                angles.append(angle)
        if len(set(angles)) > bestsitecount:
            bestsitecount = len(set(angles))
            bestsite = source
        #print(len(set(angles)))
    print("best site: ", bestsite, " and its count ", bestsitecount) 
        # for asteroid in asteroids.keys():
        #     x = 0

def test():
    calculate('10-1.test')
    calculate('10-2.test')
    calculate('10-3.test')
    calculate('10-4.test')
    calculate('10-5.test')

def part1():
    calculate('10.in')

test()
part1()

