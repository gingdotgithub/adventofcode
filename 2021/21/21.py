from functools import lru_cache

#takes gamestate+3 new dice rolls, and a players turn (always 1 or 0)
#use caching to speed it up.
@lru_cache(maxsize=None)
def roll(p1pos,p1score,p2pos,p2score,roll1,roll2,roll3, turn):
    playrs = [[p1pos,p1score],[p2pos,p2score]]
    print("doing player "+str(turn)+ ": "+str(playrs) + " - rolling: "+str(roll1)+","+str(roll2)+","+str(roll3))

    #if its a win state for whoever's go it is, return 1,0 or 0,1
    if turn == 0:
        p1pos = (((p1pos+roll1+roll2+roll3)-1)%10)+1
        p1score+=p1pos
        if  p1score>=21:
            print("returning")
            return 1,0
    else:
        p2pos = (((p2pos+roll1+roll2+roll3)-1)%10)+1
        p2score+=p2pos
        if  p2score>=21:
            print("returning")
            return 0,1

    #otherwise sum each players wins for all 27 possible roll combinations
    turn=(turn+1)%2
    result1 = 0
    result2 = 0
    for roll1 in range(1,4):
        for roll2 in range(1,4):
            for roll3 in range(1,4):
                newresult1, newresult2 = roll(p1pos,p1score,p2pos,p2score,roll1,roll2,roll3,turn)
                result1+=newresult1
                result2+=newresult2
    return result1,result2

#### main starting
#probably should have got this into the function by rearranging it, but hey
#rolls 27 combinations and sums the number of wins each leads to
mainresult1 = 0
mainresult2 = 0
for roll1 in range(1,4):
    for roll2 in range(1,4):
        for roll3 in range(1,4):
            mainnewresult1, mainnewresult2 = roll(3,0,7,0,roll1,roll2,roll3,0)
            mainresult1+=mainnewresult1
            mainresult2+=mainnewresult2
print(str(mainresult1)+","+str(mainresult2))
#print("444356092776315,341960390180808")