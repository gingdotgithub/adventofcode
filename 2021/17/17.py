#targetzone = [[20,30],[-10,-5]]
targetzone = [[14,50],[-267,-225]]
xrange = []
yrange = [abs(targetzone[1][0]),targetzone[1][0]]
maxheight = 0

def tnum(n):
    return (n*(n+1))/2

x=0
y=0
while tnum(x) < abs(targetzone[0][1]):
    if tnum(x) >= abs(targetzone[0][0]):
        xrange.append(x)
        break
    x+=1
xrange.append(targetzone[0][1])

for x in range(xrange[0],xrange[1]):
    for y in range(yrange[1],yrange[0]):
        print("trying "+str(x)+","+str(y))
        stepx = x
        stepy = y
        step = 1
        trialheight = y
        while True:
            if stepy > trialheight:
                trialheight = stepy
            if stepx >= targetzone[0][0] and stepx <= targetzone[0][1] and stepy >= targetzone[1][0] and stepy <= targetzone[1][1]:
                #hit
                if trialheight > maxheight:
                    maxheight = trialheight
                    print("new max height = " + str(maxheight))
                break
            if stepx > targetzone[0][1] or stepy < targetzone[1][0]:
                #overshoot
                break
            downstep = 1*step
            stepy+=y-(1*step)
            if x-downstep < 0:
                downstep = x
            stepx+=x-downstep
            step+=1


print(str(maxheight))
                        


