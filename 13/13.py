import itertools
coords = []
folds = []
maxy = 0
maxx = 0

def readcoords():
    global maxy
    global maxx
    global coords
    while True:
        newline = input()
        if newline == '':
            return False  
        newcoord = list(map(int,newline.split(',')))
        if newcoord[1] > maxy:
            maxy = newcoord[1]
        if newcoord[0] > maxx:
            maxx = newcoord[0]
        coords.append(newcoord)

def readfolds():
    global folds
    while True:
        newline = input()
        if newline == '':
            return False    
        parts = newline.split(" ")
        temp = parts[2].split("=")
        folds.append([temp[0],int(temp[1])])

readcoords()
readfolds()

fold = folds[0]
for coord in coords:
    if fold[0] == 'y' and coord[1] > fold[1]:
        temp = abs(coord[1]-(fold[1]*2))
        print(str(coord) + " becomes " + str([coord[0],temp]))
        coord[1] = temp
    if fold[0] == 'x' and coord[0] > fold[1]:
        temp = abs(coord[0]-(fold[1]*2))
        print(str(coord) + " becomes " + str([temp,coord[1]]))
        coord[0] = temp
coords.sort()   
print(coords)  
coords = list(coords for coords,_ in itertools.groupby(coords))
print(coords)
print(str(maxy))
print(str(maxx))
print(str(len(coords)))
