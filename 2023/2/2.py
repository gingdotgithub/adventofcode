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

def processGame(filename):
    with open(filename) as f:
        gamedata = f.readlines()

    totalscore = 0
    for game in gamedata:
        game = game.strip()
        gamemetadata = game.split(":")
        gameid = int(gamemetadata[0].split()[1])
        fistfuls = gamemetadata[1].split(";")
        # if playGame(fistfuls) == True:
        #     totalscore += gameid
        totalscore+=playRevisedGame(fistfuls)
    print(totalscore)

def test():
    print("testing:")
    processGame('2.test')

def part1():
    print("Part 1:")
    processGame('2.in')

test()
part1()