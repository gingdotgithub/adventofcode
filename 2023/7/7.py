def handtype(hand):
    counts = dict.fromkeys(hand,0)

    #processing Js as Jokers for part 2
    largestkey = "" #will add counts of jokers to this
    largestval = 0 
    for c in hand:
        counts[c] += 1
        if c != "J" and counts[c] > largestval: #tracking the most common item
            largestval = counts[c]
            largestkey = c
    if len(counts) > 1 and "J" in counts.keys(): #only works if its not five of a J
        counts[largestkey] += counts["J"] #add Js to the biggest item
        counts.pop("J")

    #now doing the hand type calculation as normal (part 1)
    if len(counts) == 1:
        print("5 of a kind")
        return 6
    elif len(counts) == 5:
        print("high card")
        return 0
    elif len(counts) == 4:
        print("pair")
        return 1
    else:
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
        

t = { #converts non-09 cards to alphabetically sortable letters instead
    "T": "a",
    "J": "1",
    "Q": "c",
    "K": "d",
    "A": "e"
}
winsorter = {} #has types of hand in it, by ID, that can be sorted. e.g. 6 is five of a kind. 5 is four of a kind, etc

with open('7.in') as f:
    hands = f.readlines()

for hand in hands:
    print(hand)
    handparts = hand.split()
    bid = int(handparts[1])
    handt = handtype(handparts[0])
    print(handt)
    newhand = "" #a string that'll hold the sortable string version from [t]ranslation
    for x in range(0,len(handparts[0])):
        if handparts[0][x] in t:
            newhand += t[handparts[0][x]]
        else:
            newhand += handparts[0][x]
    
    if handt not in winsorter.keys(): #add the type of hand to the dictionary
        winsorter[handt] = {}
    winsorter[handt][newhand] = int(handparts[1]) #dict of types of hand, as dicts (by hand) pointing to bids

print(winsorter)

counter = 0
answer = 0
for handtype in sorted(winsorter.keys()):
    for hand in sorted(winsorter[handtype].keys()):
        print("doing",hand,"-",winsorter[handtype][hand])
        counter += 1
        answer += (counter * winsorter[handtype][hand])

print(answer)
