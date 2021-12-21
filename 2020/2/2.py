validpasswords = 0

while True:
    readline = input()
    if readline == '':
        break
    parts = readline.split(" ")
    charrange = list(map(int,parts[0].split("-")))
    charcheck = parts[1][0:1]
    charcount = parts[2].count(charcheck)
    # if charcount >= charrange[0] and charcount <= charrange[1]:
    #     validpasswords += 1 
    validitycheck = 0
    if charrange[0] <= len(parts[2]) and parts[2][charrange[0]-1:charrange[0]] == charcheck:
        validitycheck += 1
    if charrange[1] <= len(parts[2]) and parts[2][charrange[1]-1:charrange[1]] == charcheck:
        validitycheck += 1
    if validitycheck == 1:
        validpasswords+=1 


print(str(validpasswords))