nsum = 0
digitletters = ['']*10
fivedletters = []
sixdletters = []
digitvalues = {}

#tells what the 5s are. 3 contains 1, otherwise 5 contains the |_ of 4. 
def solve5s():
    for digit in fivedletters:
        if all(elem in list(digit) for elem in list(digitletters[1])):
            digitletters[3] = digit
            digitvalues["".join(digit)] = 3
        else:
            four = list(digitletters[4])
            topleftmid = ''
            for n in four:
                if n not in digitletters[1]:
                    topleftmid+= n
            if all(elem in list(digit) for elem in list(topleftmid)):
                digitletters[5] = digit
                digitvalues["".join(digit)] = 5
            else:
                digitletters[2] = digit
                digitvalues["".join(digit)] = 2

#tells what the 6s are. 9 contains 4, 6 contains 5, otherwise 0.
def solve6s():
    for digit in sixdletters:
        if all(elem in list(digit) for elem in list(digitletters[4])):
            digitletters[9] = digit
            digitvalues["".join(digit)] = 9
        elif all(elem in list(digit) for elem in list(digitletters[5])):
            digitletters[6] = digit
            digitvalues["".join(digit)] = 6
        else:
            digitletters[0] = digit
            digitvalues["".join(digit)] = 0

#process all lines. extract 1,4,7,8 for being unique numbers of bits.
#stores its code in the digitletters array
#and stores value of each code in the digitvalues dictionary
#otherwise collects the 5s and 6s
while True:
    newline = input()
    if newline == '':
        break
    halves = newline.split('|')
    inputs = halves[0].split()
    for n in inputs:
        n = sorted(n)
        nlen = len(n)
        if nlen == 2:
            digitletters[1] = n
            digitvalues["".join(n)] = 1
        elif nlen == 3:
            digitletters[7] = n
            digitvalues["".join(n)] = 7
        elif nlen == 4:
            digitletters[4] = n
            digitvalues["".join(n)] = 4
        elif nlen == 7:
            digitletters[8] = n
            digitvalues["".join(n)] = 8
        elif nlen == 5:
            fivedletters.append(n)
        else:
            sixdletters.append(n)

    solve5s()
    fivedletters = []
    solve6s()
    sixdletters = []

    #process output values, using sortedversion of string again to match
    outputstring = ''
    for n in halves[1].split():
        outputstring+=str(digitvalues["".join(sorted(n))])
    nsum+=int(outputstring)

print(str(nsum))