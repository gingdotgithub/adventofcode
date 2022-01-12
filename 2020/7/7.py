bags = {}

while True:
    newline = input()
    if newline == '':
        break
    lineparts = newline.split()
    newbag = lineparts[0] + " " + lineparts[1]
    x = 4
    bagcontents = []
    if lineparts[x] != 'no':
        while x < len(lineparts):
            bagcontents.append(int(lineparts[x]))
            bagcontents.append(lineparts[x+1] + " " + lineparts[x+2])
            x+=4
    #maybe else append a 0 for no contents
    bags[newbag] = bagcontents

print(bags)

def what_bags(target):
    global bags
    count_num_bags = 0
    for bagtype in bags.keys():
        if check_bag(bagtype,target):
            count_num_bags+=1
    return count_num_bags

def check_bag(bagtocheck,target):
    global bags
    x = 1
    while x < len(bags[bagtocheck]):
        if bags[bagtocheck][x] == target or check_bag(bags[bagtocheck][x],target):
            return True
        x+=2
    return False


print(what_bags('shiny gold'))