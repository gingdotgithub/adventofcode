import time
import re

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



answer = 0
for vals in values:
    if process(vals,rules['in']) == "A":
        print("got an A, vals are",vals)
        answer+=sum(vals)
endtime = time.time()
print("part 1:",answer)
print("timing:",endtime-starttime)