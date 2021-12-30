pcount = 0
reqcomponents = {'byr':0,'iyr':0,'eyr':0,'hgt':0,'hcl':0,'ecl':0,'pid':0}
passports = []
optcomponents = ['cid']
processcount = 0

def validate_data(dtype,inputval):
    if dtype == 'byr' and inputval.isnumeric():
        year = int(inputval)
        if 1920 <= year <= 2002:
            return True
    elif dtype == 'iyr' and inputval.isnumeric():
        year = int(inputval)
        if 2010 <= year <= 2020:
            return True
    elif dtype == 'eyr' and inputval.isnumeric():
        year = int(inputval)
        if 2020 <= year <= 2030:
            return True
    elif dtype == 'hgt' and ("in" in inputval or "cm" in inputval):
        measuretype = inputval[-2:]
        measureval = int(inputval[0:-2])
        if measuretype == 'in' and 59 <= measureval <= 76:
            return True
        elif measuretype == 'cm' and 150 <= measureval <= 193:
            return True
    elif dtype =='hcl':
        if len(inputval) == 7:
            sixcheck = 0
            for i in range(len(inputval)):
                if inputval[i+1:i+2] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                    sixcheck+=1
            if sixcheck == 6:
                return True
    elif dtype == 'ecl':
        if inputval in ['amb','blu','brn','gry','grn','hzl','oth']:
            return True
    elif dtype == 'pid' and inputval.isnumeric() and len(inputval) == 9:
        return True
    return False


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
                if validate_data(part[0],part[1]):
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