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
    bestsetangles = {} #a dict that will be a set of all angles from the best site's point of view
    for source in asteroids.keys():
        angles = {} #converted to a dict for part 2, to hold a list for every angle
        for asteroid in asteroids.keys():
            if asteroid != source:
                angle = math.atan2(asteroid[0]-source[0],asteroid[1]-source[1])
                distance = math.sqrt((asteroid[0]-source[0])**2) + ((asteroid[1]-source[1])**2) #calc distance for part 2, as we go
                #print(angle)
                if angle not in angles.keys():
                    angles[angle] = {} #also a dict, holding a coordinate for evey distance, so we can sort by distance later
                angles[angle][distance] = asteroid
        if len(angles.keys()) > bestsitecount:
            bestsitecount = len(angles.keys())
            bestsite = source
            #print(angles)
            bestsetangles = angles.copy()
        #print(len(set(angles)))
    print("best site: ", bestsite, " and its count ", bestsitecount) 
    return dict(sorted(bestsetangles.items(),key=lambda x:x[0],reverse=True)) #reverse because north is the biggest angle from atan2
        # for asteroid in asteroids.keys():
        #     x = 0

def test():
    calculate('10-1.test')
    calculate('10-2.test')
    calculate('10-3.test')
    calculate('10-4.test')
    calculate('10-5.test')

def part1():
    return calculate('10.in')

def part2(bestsetangles):
    #print(bestsetangles)
    counter = 0
    for angle in bestsetangles.keys():
        bestsetangles[angle] = dict(sorted(bestsetangles[angle].items()))
        if len(bestsetangles[angle].keys()) > 0:
            counter = counter + 1
            angledists = list(bestsetangles[angle].keys())
            #print(angledists[0])
            if counter == 200:
                print((bestsetangles[angle][angledists[0]][0]*100)+bestsetangles[angle][angledists[0]][1])

            del bestsetangles[angle][angledists[0]]
        else:
            del bestsetangles[angle]
        


test()
bestsetangles = part1()
part2(bestsetangles.copy())
