players = []
#player = space,score
players.append([3,0])
players.append([7,0])
#turnstaken = 0
ddice = 0
turn = 0

while players[0][1]<1000 and players[1][1]<1000:
    ddice+=1
    roll1 = ddice
    ddice+=1
    roll2 = ddice
    ddice+=1
    roll3 = ddice
    players[turn%2][0] = (((players[turn%2][0]+roll1+roll2+roll3)-1)%10)+1
    players[turn%2][1]+=players[turn%2][0]
    turn+=3

print(min(players[0][1],players[1][1])*turn)
