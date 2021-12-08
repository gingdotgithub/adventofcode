nsum = 0
digitletters = ['']*10
fivedletters = []
sixdletters = []
digitvalues = {}

def solve5s():
    for digit in fivedletters:
        # temp1 = list(digitletters[1])
        # temp2 = list(digit)
        # doescontain = all(elem in list(digitletters[1]) for elem in list(digit))
        if all(elem in list(digit) for elem in list(digitletters[1])):
            digitletters[3] = digit
            digitvalues["".join(sorted(digit))] = 3
        else:
            four = list(digitletters[4])
            topleftmid = ''
            for n in four:
                if n not in digitletters[1]:
                    topleftmid+= n
            if all(elem in list(digit) for elem in list(topleftmid)):
                digitletters[5] = digit
                digitvalues["".join(sorted(digit))] = 5
            else:
                digitletters[2] = digit
                digitvalues["".join(sorted(digit))] = 2

def solve6s():
    for digit in sixdletters:
        if all(elem in list(digit) for elem in list(digitletters[4])):
            digitletters[9] = digit
            digitvalues["".join(sorted(digit))] = 9
        elif all(elem in list(digit) for elem in list(digitletters[5])):
            digitletters[6] = digit
            digitvalues["".join(sorted(digit))] = 6
        else:
            digitletters[0] = digit
            digitvalues["".join(sorted(digit))] = 0

while True:
    newline = input()
    if newline == '':
        break
    halves = newline.split('|')
    inputs = halves[0].split()
    for n in inputs:
        nlen = len(n)
        if nlen == 2:
            digitletters[1] = n
            digitvalues["".join(sorted(n))] = 1
        elif nlen == 3:
            digitletters[7] = n
            digitvalues["".join(sorted(n))] = 7
        elif nlen == 4:
            digitletters[4] = n
            digitvalues["".join(sorted(n))] = 4
        elif nlen == 7:
            digitletters[8] = n
            digitvalues["".join(sorted(n))] = 8
        elif nlen == 5:
            fivedletters.append(n)
        else:
            sixdletters.append(n)

    solve5s()
    fivedletters = []
    solve6s()
    sixdletters = []
    print(digitletters)
    print(digitvalues)

    outputstring = ''
    for n in halves[1].split():
        outputstring+=str(digitvalues["".join(sorted(n))])
    nsum+=int(outputstring)

print(str(nsum))