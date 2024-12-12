import time

time1=time.time()
with open('12.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]
time2=time.time()

visited = []
tovisit = []
currregion = []
h = len(dataset)
w = len(dataset[0])
for y in range(h):
    for x in range(w):
        tovisit.append([x,y])
regions = {}
URC = 0 #unique region counter
directions = [[0,-1],[1,0],[0,1],[-1,0]]

#FIND ALL REGIONS
while len(tovisit) > 0:
    newcell = tovisit.pop(0)
    currregion = [newcell]
    visited.append(newcell)
    #start exploring a new region
    x = 0
    while x < len(currregion):
        cell = currregion[x]
        # print("current cell",cell)
        # print("value is",dataset[cell[1]][cell[0]])
        for dir in directions:
            neighbour = [cell[0]+dir[0],cell[1]+dir[1]]
            if neighbour not in visited and neighbour not in currregion:
                if neighbour[0] >= 0 and neighbour[0] < w and neighbour[1] >= 0 and neighbour[1] < h:
                    # print("neighbour cell",neighbour,"is",dataset[neighbour[1]][neighbour[0]])
                    if dataset[cell[1]][cell[0]] == dataset[neighbour[1]][neighbour[0]]:
                        currregion.append(neighbour)
                        tovisit.remove(neighbour)
        x+=1
    regions[URC] = currregion.copy()
    URC+=1

time3 = time.time()

#find part 1 borders
borders = {}
for regionkey in regions.keys():
    region = regions[regionkey]
    b = 0
    for cell in region:
        for dir in directions:
            neighbour = [cell[0]+dir[0],cell[1]+dir[1]]
            if neighbour not in region:
                b+=1
    borders[regionkey] = b

# print(borders)

total = 0
for regionkey in regions.keys():
    total += (len(regions[regionkey])*borders[regionkey])
print("part 1:",total)
time4 = time.time()


#PART 2 STUFF

#minmax returns the lowest x and y and highest x and y for creating slices
def minmax(region):
    minx = w
    miny = h
    maxx = 0
    maxy = 0
    # print(region)
    for cell in region:
        if cell[0] < minx:
            minx = cell[0]
        if cell[0] > maxx:
            maxx = cell[0]
        if cell[1] < miny:
            miny = cell[1]
        if cell[1] > maxy:
            maxy = cell[1]
    # print(minx,miny,maxx,maxy)
    return minx, miny, maxx, maxy

#vslice returns a vertical slice for a given x coord
def vslice(forx, region):
    cells = []
    for cell in region:
        if cell[0] == forx:
            cells.append(cell[1])
    cells.sort()
    return cells

#hslice returns a vertical slice for a given y coord
def hslice(fory, region):
    cells = []
    for cell in region:
        if cell[1] == fory:
            cells.append(cell[0])
    cells.sort()
    return cells


print("doing part 2")

newborders = {}
# print(regions)
for regionkey in regions.keys():
    total = 0
    region = regions[regionkey]
    minx, miny, maxx, maxy = minmax(region)

    #loop 1 processes vertical slices in the minmax x of the region
    for x in range(minx,maxx+1):
        slice = vslice(x,region)
        # print("vertical slice is:",slice)
        sliceisleftborder = []
        sliceisrightborder = []
        count = 0
        #figure out which items in the slice are left border and/or right border cells
        for i in range(len(slice)):
            if [x-1,slice[i]] not in region:
                sliceisleftborder.append(slice[i])
            # print("leftborder:",sliceisleftborder)
            if [x+1,slice[i]] not in region:
                sliceisrightborder.append(slice[i])
            # print("right border:",sliceisrightborder)
        #if there is any left border, add 1
        if len(sliceisleftborder) > 0:
            count += 1
        #if there is any right border, add 1
        if len(sliceisrightborder) > 0:
            count += 1
        #check for any non-contiguous bits of the left border, and increment if so
        #123/56 would add 1
        #12/45/78 would add 2
        for i in range(len(sliceisleftborder)-1):
            if sliceisleftborder[i+1] != sliceisleftborder[i]+1:
                count+=1
        #check for any non-contiguous bits of the right border, and increment if so
        for i in range(len(sliceisrightborder)-1):
            if sliceisrightborder[i+1] != sliceisrightborder[i]+1:
                count+=1
        total+=count
    #repeat above for horizontal slices checking for top and bottom borders
    for y in range(miny,maxy+1):
        slice = hslice(y,region)
        # print("horizontal slice is:",slice)
        count = 0
        sliceistopborder=[]
        sliceisbottomborder=[]
        for i in range(len(slice)):
            if [slice[i],y-1] not in region:
                sliceistopborder.append(slice[i])
            # print("top border:",sliceistopborder)
            if [slice[i],y+1] not in region:
                sliceisbottomborder.append(slice[i])
            # print("bottom bottom:",sliceisbottomborder)
        if len(sliceistopborder) > 0:
            count+=1
        if len(sliceisbottomborder) > 0:
            count+=1
        for i in range(len(sliceistopborder)-1):
            if sliceistopborder[i+1] != sliceistopborder[i]+1:
                count+=1
        for i in range(len(sliceisbottomborder)-1):
            if sliceisbottomborder[i+1] != sliceisbottomborder[i]+1:
                count+=1
        total+=count
    # print("current total:",total)
    # store the new border cost for the region
    newborders[regionkey] = total

newprice = 0
for regionkey in regions.keys():
    newprice += (len(regions[regionkey])*newborders[regionkey])
print("Part 2:",newprice)
time5 = time.time()
print("Finding regions",int((time3-time2)*1000),"ms")
print("Part 1 borders:",int((time4-time3)*1000),"ms")
print("Part 2 borders:",int((time5-time4)*1000),"ms")

