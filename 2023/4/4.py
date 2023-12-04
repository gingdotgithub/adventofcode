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
        print(cardid,overlapping)
        if len(overlapping) > 0:
            answer+= 2**(len(overlapping)-1)

    print(answer)

part1('4.in')
#part1('4.test')