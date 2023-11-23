orbitMap = {}
depthMap = {}

def test():
    orbitMap.clear()
    depthMap.clear()
    with open('6.test') as f:
        buildmap(f.readlines())
    countOrbits('COM',0)
    print(sum(depthMap.values()))


def buildmap(orbits):
    for orbit in orbits:
        orbitParts = orbit.strip().split(")")
        print(orbitParts)
        if orbitParts[0] not in orbitMap.keys():
            orbitMap[orbitParts[0]] = []
        orbitMap[orbitParts[0]].append(orbitParts[1])

    print(orbitMap)


def countOrbits(parent,depth):
    depthMap[parent] = depth
    if parent in orbitMap.keys():
        depth = depth + 1
        for orbit in orbitMap[parent]:
            countOrbits(orbit,depth)


def part1():
    orbitMap.clear()
    depthMap.clear()
    with open('6.in') as f:
        buildmap(f.readlines())
    countOrbits('COM',0)
    print(sum(depthMap.values()))

test()
part1()