orbitMap = {}
depthMap = {}
pathMap = {}

def test():
    orbitMap.clear()
    depthMap.clear()
    pathMap.clear()
    with open('6.test') as f:
        buildmap(f.readlines())
    countOrbits('COM',0,[])
    print(sum(depthMap.values()))
    print(pathMap)


def buildmap(orbits):
    for orbit in orbits:
        orbitParts = orbit.strip().split(")")
        print(orbitParts)
        if orbitParts[0] not in orbitMap.keys():
            orbitMap[orbitParts[0]] = []
        orbitMap[orbitParts[0]].append(orbitParts[1])

    print(orbitMap)


def countOrbits(parent,depth,path):
    depthMap[parent] = depth
    pathMap[parent] = path.copy()
    if parent in orbitMap.keys():
        depth = depth + 1
        newpath = path.copy()
        newpath.append(parent)
        for orbit in orbitMap[parent]:
            countOrbits(orbit,depth,newpath)


def part1():
    orbitMap.clear()
    depthMap.clear()
    pathMap.clear()
    with open('6.in') as f:
        buildmap(f.readlines())
    countOrbits('COM',0,[])
    print(sum(depthMap.values()))

def part2():
    PTY = set(pathMap['YOU'].copy())
    PTS = set(pathMap['SAN'].copy())
    print(len(PTY ^ PTS))




test()
part1()
part2()