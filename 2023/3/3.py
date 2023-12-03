numbers = {}
symbols = {}

def check(xrange,yrange):
    for x in xrange:
        for y in yrange:
            if (x,y) in symbols.keys():
                print("found symbol",symbols[(x,y)])
                return True
    return False

def processGrid():
    with open('3.in') as f:
        engine = f.readlines()

    currnumber = ""
    for y in range(0,len(engine)):
        line = engine[y].strip()
        #print(line)
        for x in range(0,len(line)):
            if line[x].isnumeric():
                currnumber += line[x]
            else:
                #print(currnumber)
                if currnumber != "":
                    currgrid = (x-len(currnumber),y)
                    #print(currgrid,currnumber)
                    numbers[currgrid] = currnumber
                    currnumber = ""
                if line[x] != ".":
                    symbols[(x,y)] = line[x]
        if currnumber != "":
            currgrid = ((len(line)-1)-len(currnumber),y)
            #print(currgrid,currnumber)
            numbers[currgrid] = currnumber
            currnumber = ""

    print(symbols)
    print(numbers)

def part1():
    answer = 0
    for gridrefx,gridrefy in numbers:
        xrange = range(gridrefx-1,gridrefx+len(numbers[(gridrefx,gridrefy)])+1)
        yrange = range(gridrefy-1,gridrefy+2)
        #print(xrange, yrange)
        if check(xrange,yrange) == True:
            print("found symbol, adding",numbers[(gridrefx,gridrefy)])
            answer += int(numbers[(gridrefx,gridrefy)])
    print(answer)

processGrid()
part1()