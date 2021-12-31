from collections import Counter
groupanswers = []

def process_group(newline):
    thisgroup = Counter()
    people = 0
    while True:
        if newline == '':
            outcomes = []
            for key,value in thisgroup.most_common():
                if value < people:
                    break
                outcomes.append(key)
            groupanswers.append(outcomes)
            return
        for x in newline:
            #if x not in thisgroup.keys():
            thisgroup[x]+=1
        newline = input()
        people+=1


while True:
    newline = input()
    if newline == '':
        break
    process_group(newline)

print(groupanswers)
print(sum(len(a) for a in groupanswers))