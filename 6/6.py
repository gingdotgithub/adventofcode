from time import process_time
fishinput = input().split(',')
starttime = process_time()
DAY_TARGET = 256
fishpotential=[1]*DAY_TARGET
fishpotential[0] = 0

#precalculates the number of fish that get created 
#as a consequence of being created on day x
def calcfishpotential():
    for x in range(8,DAY_TARGET-1):
        newfishpotential = 1
        print(str(newfishpotential))
        y = x-8
        while y >= 0:
            print("y is " + str(y))
            newfishpotential+=fishpotential[y]
            y-=7
        fishpotential[x+1]=newfishpotential

#looks like [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5]
calcfishpotential()
print(fishpotential)

fishcount=0
for fish in fishinput:
    #count itself
    fishcount+=1
    #start howevermany days after
    x = DAY_TARGET-int(fish)
    #cycle through the fishpotential array to see how many fish it creates
    while x >= 0:
        fishcount+=fishpotential[x]
        x-=7
print(str(fishcount))
print('took: '+str(process_time()-starttime))
