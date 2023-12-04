wincounts = {}
cardcounts = {}

def part1(filename):
    with open(filename) as f:
        cards = f.readlines()

    answer = 0
    for card in cards:
        cardid, cnums = card.strip().split(":")
        winning, received = cnums.split("|")
        wnums = winning.split()
        rnums = received.split()
        overlapping = set(wnums) & set(rnums)
        #print(cardid,overlapping)
        cardnum = cardid.split()
        wincounts[cardnum[1]] = len(overlapping) #for part 2
        cardcounts[cardnum[1]] = 1 #for part 2
        if len(overlapping) > 0:
            answer+= 2**(len(overlapping)-1)

    print("Part 1:",answer)

def part2():
    for x in range(1,len(wincounts)+1):
        for n in range(0,wincounts[str(x)]):
            cardcounts[str(x+1+n)] += cardcounts[str(x)]
        #print("doing card ",x,"-",cardcounts)
    print("Part 2:",sum(cardcounts.values()))

part1('4.in')
#part1('4.test')
part2()