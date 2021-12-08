ncount = 0
while True:
    newline = input()
    if newline == '':
        break
    halves = newline.split('|')
    outputs = halves[1].split()
    for n in outputs:
        nlen = len(n)
        if nlen <5 or nlen == 7:
            ncount+= 1

print(str(ncount))
