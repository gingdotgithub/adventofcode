from collections import Counter

def test():

    with open('4.test') as f:
        for passcode in f.readlines():
            result = checkPasscode(passcode.strip())
            print(result)

def checkPasscode(passcode):
    includesTwo = False
    validPasscode = True
    for x in range(0,len(passcode)-1):
        if passcode[x+1] == passcode[x]:
            includesTwo = True
        elif passcode[x+1] < passcode[x]:
            validPasscode = False
            return False
    return validPasscode and includesTwo

def check2Max(passcode):
    numCheck = Counter(passcode)
    if 2 in numCheck.values():
        return True
    return False


def part1():
    validCounter = 0
    for x in range(128392,643281):
        if checkPasscode(str(x)):
            validCounter = validCounter + 1
    print(validCounter)

def part2():
    validCounter = 0
    for x in range(128392,643281):
        passcode = str(x)
        if checkPasscode(passcode):
            if check2Max(passcode):
                validCounter = validCounter + 1
    print(validCounter)


test()
part1()
part2()