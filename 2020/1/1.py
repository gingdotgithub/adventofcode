readvalues = []
while True:
    newline = input()
    if newline == '':
        break
    readvalues.append(newline)

for readvalue in readvalues:
    if str(2020-int(readvalue)) in readvalues:
        print(str(int(readvalue)*(2020-int(readvalue))))
        break
