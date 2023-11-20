
def part1test():
    with open('2.test') as f:
        originalinput = list(map(int,f.readline().split(",")))
    testinput = originalinput
    testoutput = process(testinput)
    print(testoutput[0])

def part1():
    with open('2.in') as f:
        originalinput = list(map(int,f.readline().split(",")))
    part1input = originalinput
    part1input[1] = 12
    part1input[2] = 2
    part1output = process(part1input)
    
    print(part1output)
    print(part1output[0])

def process(taskinput):
    #print(taskinput)
    #print(len(taskinput))
    for x in range(0,len(taskinput),4):
        #print(taskinput[x])
        
        y=taskinput[x]
        if y == 1:
            taskinput[taskinput[x+3]] = taskinput[taskinput[x+1]]+taskinput[taskinput[x+2]]
        elif y == 2:
            taskinput[taskinput[x+3]] = taskinput[taskinput[x+1]]*taskinput[taskinput[x+2]]
        elif y == 99:
            print("breaking")
            break
        else:
            print("didnt find it")
            break
        #print(taskinput)

    return taskinput

originalinput = []
part1test()    
part1()
