validpasswords = 0

while True:
    readline = input()
    if readline == '':
        break
    parts = readline.split(" ")
    charrange = list(map(int,parts[0].split("-")))
    charcheck = parts[1][0:1]
    charcount = parts[2].count(charcheck)
    if charcount >= charrange[0] and charcount <= charrange[1]:
        validpasswords += 1 

print(str(validpasswords))