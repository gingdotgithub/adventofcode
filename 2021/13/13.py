import itertools
coords = []
folds = []
lasty = 0
lastx = 0

def readcoords():
    global coords
    while True:
        newline = input()
        if newline == '':
            return False  
        newcoord = list(map(int,newline.split(',')))
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

for fold in folds:
    for coord in coords:
        if fold[0] == 'y' and coord[1] > fold[1]:
            temp = abs(coord[1]-(fold[1]*2))
            print(str(coord) + " becomes " + str([coord[0],temp]))
            coord[1] = temp
            lasty = fold[1]
        if fold[0] == 'x' and coord[0] > fold[1]:
            temp = abs(coord[0]-(fold[1]*2))
            print(str(coord) + " becomes " + str([temp,coord[1]]))
            coord[0] = temp
            lastx = fold[1]
    coords.sort()   
    #print(coords)  
    coords = list(coords for coords,_ in itertools.groupby(coords))
    
print(coords)
print(str(len(coords)))
for y in range(lasty):
    output = ""
    for x in range(lastx):
        if [x,y] in coords:
            output+="#"
        else:
            output+= "."
    print(output)
