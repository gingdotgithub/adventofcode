pcount = 0
reqcomponents = {'byr':0,'iyr':0,'eyr':0,'hgt':0,'hcl':0,'ecl':0,'pid':0}
passports = []
optcomponents = ['cid']
processcount = 0

def read_passport(newline):
    global reqcomponents
    global pcount
    global processcount
    processcount+=1
    components = reqcomponents.copy()
    while True:
        if newline == '':
            passports.append(components)
            return
        parts = newline.split()
        for x in range(len(parts)):
            part = parts[x].split(":")
            if part[0] in components.keys():
                components[part[0]]+=1
        newline = input()

while True:
    newline = input()
    if newline == '':
        break
    read_passport(newline)

for pp in passports:
    print(pp)
    if sum(pp.values()) == 7:
        pcount+=1

print(pcount)