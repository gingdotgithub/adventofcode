groupanswers = []

def process_group(newline):
    thisgroup = []
    while True:
        if newline == '':
            groupanswers.append(thisgroup)
            return
        for x in newline:
            if x not in thisgroup:
                thisgroup.append(x)
        newline = input()


while True:
    newline = input()
    if newline == '':
        break
    process_group(newline)

print(groupanswers)
print(sum(len(a) for a in groupanswers))