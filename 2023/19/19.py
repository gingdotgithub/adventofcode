import time

data = open('19.in').read().splitlines()
starttime = time.time()

rules = {}
values = []
rulesdone = False
for row in data:
    if not rulesdone and row != "":
        rid,rule = row[:-1].split("{")
        rules[rid] = rule
    if row == "":
        rulesdone = True
        continue
    if rulesdone:
        vals = []
        parts = row[1:-1].split(",")
        for part in parts:
            _,val = part.split("=")
            vals.append(int(val))
        values.append(tuple(vals))

# print(rules)
# print(values)

def process(values,checks):
    print(values,"vals with",checks)
    if ":" not in checks:
        print("no more rules to check")
        if checks in "AR":
            print("returning",checks)
            return checks
        else:
            return process(values,rules[checks])
    else:
        checks = checks.split(",")
        x,m,a,s = values
        condition,outcome = checks[0].split(":")
        print("outcome of",condition,"is",eval(condition))
        if eval(condition):
            if outcome in "AR": 
                print("returning",outcome)
                return outcome
            else:
                print("will next process:",rules[outcome])
                return process(values,rules[outcome])
        else:
            return process(values,",".join(checks[1:]))


def part1():
    answer = 0
    for vals in values:
        if process(vals,rules['in']) == "A":
            print("got an A, vals are",vals)
            answer+=sum(vals)
    endtime = time.time()
    print("part 1:",answer)
    print("timing:",endtime-starttime)

#part1()

def process2(valranges,checks):
    print("doing",checks)
    if ":" not in checks:
        if checks in "AR":
            if checks == "A": #if found and A state, add the ranges to the dict used to calc the answer. #R state does nothing
                for char in range(0,4):
                    print("adding","xmas"[char],valranges[char])
                    valrangedict["xmas"[char]].append(valranges[char]) 
                print(valrangedict)
        else:
            process2(valranges,rules[checks]) #if its state is just to point to another rule, but no condition, then process the ranges with it
    else:
        checks = checks.split(",") #this section basically splits reads in the rule
        x,m,a,s = valranges
        condition,outcome = checks[0].split(":")
        char = condition[0:1]
        comparison = condition[1:2]
        value = int(condition[2:])
        adder = 0 #this little bit here is creating two new ranges depending on the condition of the rule, low range and high range
        if comparison == ">": 
            adder = 1 #this plus one is just adjsuting the border to be definitely above the value. its just playing with borders to be accurate.
        print(char,comparison,value)
        relevantrange = eval(char)
        lowrange = (min(relevantrange),value+adder-1)
        highrange = (value+adder,max(relevantrange))
        print("splitting:",relevantrange,"into",lowrange,highrange)

        if comparison == ">": #if its a greater than rule...
            lowranges = valranges.copy()
            lowranges["xmas".index(char)] = lowrange
            print(lowranges,"going to",",".join(checks[1:]))
            process2(lowranges,",".join(checks[1:])) #process the bit below the boundary with the next rule
            highranges = valranges.copy()
            highranges["xmas".index(char)] = highrange
            if outcome in "AR": #for the bit that is above the boundary, if the instruction is an accept state, send it with that
                print(highranges,"going to",outcome)
                process2(highranges,outcome)
            else: #but if its the id of a new set of rules, then send the whole new set of rules.
                print(highranges,"going to",rules[outcome])
                process2(highranges,rules[outcome])
        elif comparison == "<": #repeat logic above but for a less-than condition.
            lowranges = valranges.copy()
            lowranges["xmas".index(char)] = lowrange
            if outcome in "AR":
                print(lowranges,"going to",outcome)
                process2(lowranges,outcome)
            else:
                print(lowranges,"going to",rules[outcome])
                process2(lowranges,rules[outcome])
            highranges = valranges.copy()
            highranges["xmas".index(char)] = highrange
            print(highranges,"going to",",".join(checks[1:]))
            process2(highranges,",".join(checks[1:]))


valrangedict = { #this gets populated when an A state is found
    'x': [],
    'm': [],
    'a': [],
    's': []
}

def part2():
    result = process2([(1,4000),(1,4000),(1,4000),(1,4000)],rules['in'])
    answer2 = 0
    for n in range(0,len(valrangedict['x'])): #the nth item of each of x,m,a,s are related ebcause the got appended at the same time
        x = max(valrangedict['x'][n])-min(valrangedict['x'][n])+1 #plus one to include the upper boundary
        m = max(valrangedict['m'][n])-min(valrangedict['m'][n])+1
        a = max(valrangedict['a'][n])-min(valrangedict['a'][n])+1
        s = max(valrangedict['s'][n])-min(valrangedict['s'][n])+1 
        answer2+=(x*m*a*s) 
    endtime = time.time()
    print("part 2:",answer2)
    print("part 2 timing:",endtime-starttime)

part2()
