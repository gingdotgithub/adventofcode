import re

def process(filename, addfilter):
    with open(filename) as f:
        dataset = f.readlines()

    output = 0
    for line in dataset:

        if addfilter:
            line = findReplacements(line, False)
            line = findReplacements(line, True)

        numbers = re.sub("[^0-9]","",line)
        calibration = str(numbers[0]) + str(numbers[len(numbers)-1])
        output = output + int(calibration)
    return output

def findReplacements(line, rightToLeft):
    conv = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    if rightToLeft:
        temp = 1
        for x in range(len(line)-1,0,-1):
            if line[x].isnumeric():
                print("sub not needed")
                return line
            for c in conv.keys():
                if (x+len(c)) < len(line):
                    if line[x:x+len(c)] == c:
                        newline = line[0:x] + conv[c] + line[x+len(c):]
                        print("RtL replaced",c,"with",conv[c],".",line," is now ", newline)
                        return newline
    else: 
        for x in range(0,len(line)-2):
            if line[x].isnumeric():
                print("sub not needed")
                return line
            for c in conv.keys():
                if (x+len(c)) < len(line):
                    if line[x:x+len(c)] == c:
                        newline = line[0:x] + conv[c] + line[x+len(c):]
                        print("Replaced",c,"with",conv[c],".",line," is now ", newline)
                        return newline
    print("none found", line)
    return line


def test():
    print("test answer is:",process('1.test', False))

def test2():
    print("second test:", process('1-2.test', True))

def part1():
    print("part 1:",process('1.in', False))

def part2():
    print("part 2:", process('1.in', True))

test()
test2()
part1()
part2()