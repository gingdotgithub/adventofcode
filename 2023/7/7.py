def handtype(hand):
    cards = set(hand)
    if len(cards) == 1:
        print("5 of a kind")
        return 6
    elif len(cards) == 5:
        print("high card")
        return 0
    elif len(cards) == 4:
        print("pair")
        return 1
    else:
        counts = dict.fromkeys(hand,0)
        for c in hand:
            counts[c] += 1
        #print(counts)
        if len(counts) == 2:
            if 4 in counts.values():
            #if counts[0] == 4 or counts[1] == 4:
                print("4 of a kind")
                return 5
            if 3 in counts.values() and 2 in counts.values():
            #if (counts[0] == 3 and counts[0] == 2):
                print("full house")
                return 4
        else:
            if 3 in counts.values():
            #if counts[0] == 3 or counts[1] == 3 or counts[2] == 3:
                print("3 of a kind")
                return 3
    print("two pairs")
    return 2
        


t = {
    "T": "a",
    "J": "b",
    "Q": "c",
    "K": "d",
    "A": "e"
}
winsorter = {}

with open('7.in') as f:
    hands = f.readlines()

for hand in hands:
    print(hand)
    handparts = hand.split()
    bid = int(handparts[1])
    handt = handtype(handparts[0])
    print(handt)
    newhand = ""
    for x in range(0,len(handparts[0])):
        if handparts[0][x] in t:
            newhand += t[handparts[0][x]]
        else:
            newhand += handparts[0][x]
    
    if handt not in winsorter.keys():
        winsorter[handt] = {}
    winsorter[handt][newhand] = int(handparts[1])

print(winsorter)

counter = 0
answer = 0
for handtype in sorted(winsorter.keys()):
    for hand in sorted(winsorter[handtype].keys()):
        print("doing",hand,"-",winsorter[handtype][hand])
        counter += 1
        answer += (counter * winsorter[handtype][hand])

print(answer)
print("b">"a")