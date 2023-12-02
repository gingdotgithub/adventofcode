def playGame(fistfuls):
    limits = {
        "green": 13,
        "red": 12,
        "blue": 14
    }

    for fistful in fistfuls:
        cubes = fistful.split(",")
        for cube in cubes:
            info = cube.split()
            if int(info[0]) > limits[info[1]]:
                return False
    return True

def playRevisedGame(fistfuls):
    minimums = {
        "green": 0,
        "red": 0,
        "blue": 0
    }
    for fistful in fistfuls:
        cubes = fistful.split(",")
        for cube in cubes:
            info = cube.split()
            if int(info[0]) > minimums[info[1]]:
                minimums[info[1]] = int(info[0])
    return minimums["green"] * minimums["red"] * minimums["blue"]

def processGame(filename,part2):
    with open(filename) as f:
        gamedata = f.readlines()

    totalscore = 0
    for game in gamedata:
        game = game.strip()
        gamemetadata = game.split(":")
        gameid = int(gamemetadata[0].split()[1])
        fistfuls = gamemetadata[1].split(";")
        if part2 == False:
            if playGame(fistfuls) == True:
                totalscore += gameid
        else:
            totalscore+=playRevisedGame(fistfuls)
    print(totalscore)

def test():
    print("testing part 1:")
    processGame('2.test',False)

def part1():
    print("Part 1:")
    processGame('2.in', False)

def test2():
    print("testing part 2:")
    processGame('2.test',True)

def part2():
    print("Part 2:")
    processGame('2.in', True)

test()
part1()
test2()
part2()