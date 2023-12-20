import time
import math

data = open('20.in').read().splitlines()
starttime = time.time()

modules = {}
globalqueue = []
conjcounts = {}
cyclelengths = {"gt":-1,"vr":-1,"nl":-1,"lr":-1} #part 2: these feed into rx in my input

for row in data:
    row = row.split(" -> ")
    if row[0] == "broadcaster":
        modules[row[0]] = [0,row[1]]
    elif row[0][0:1] == "%":
        modules[row[0][1:]] = [1,row[1],0]
    else:
        modules[row[0][1:]] = [2,row[1],{}]
    for dest in row[1].split(", "):
        if dest not in conjcounts:
            conjcounts[dest] = 0
        conjcounts[dest] += 1
# print(conjcounts)
startmodule = 'broadcaster'
signal = 0 #0 is low, 1 is high

pulsecounts = {0:0,1:0}
rxnotfound = 0
rxcount = []

n = 0
while True:
    pulsecounts[0]+=1
    globalqueue.append((startmodule,"button0"))
    while len(globalqueue) > 0:
        module,signal = globalqueue.pop(0)
        sender = signal[:-1]
        signal = int(signal[-1:])

        modtype = modules[module][0]
        destinations = modules[module][1].split(", ")
        if modtype == 0:
            for dest in destinations:
                pulsecounts[signal]+=1
                if dest in modules:
                    globalqueue.append((dest,module+str(signal)))
                if module in cyclelengths and sendingsignal == 1:
                    cyclelengths[module] = n+1 #+1 because it would actually be the next cycle

        elif modtype == 1:
            if signal == 0:
                modules[module][2] = 1-modules[module][2]
                sendingsignal = modules[module][2]
                for dest in destinations:
                    pulsecounts[sendingsignal]+=1
                    if dest in modules:
                        globalqueue.append((dest,module+str(sendingsignal)))
                    if module in cyclelengths and sendingsignal == 1:
                        cyclelengths[module] = n+1
        elif modtype == 2:
            modules[module][2][sender] = signal
            sendingsignal = 1
            if len(modules[module][2]) == conjcounts[module] and set(modules[module][2].values()) == {1}:
                sendingsignal = 0
            for dest in destinations:
                pulsecounts[sendingsignal]+=1
                if dest in modules:
                    globalqueue.append((dest,module+str(sendingsignal)))
                if module in cyclelengths and sendingsignal == 1:
                    cyclelengths[module] = n+1

        #f = input("?")            
        # print(globalqueue)
    
    if -1 not in cyclelengths.values():
        break

    # print("pulse counts:",pulsecounts)
    # print("cycle lengths",cyclelengths)
    #f = input("?")
    n+=1
    rxnotfound = 0

# endtime = time.time()
# print("high pulses:",pulsecounts[1])
# print("low pulses:",pulsecounts[0])
# print("part 1:",(pulsecounts[0]*pulsecounts[1]))
# print("part 1 timing:",endtime-starttime)

# print(cyclelengths)

answer2 = math.lcm(*cyclelengths.values())
endtime = time.time()
print("part 2",answer2)
print("part 2 timing:",endtime-starttime)
    
