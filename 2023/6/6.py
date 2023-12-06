import math

distances = []
times = []

def process(filename):
    with open(filename) as f:
        data = f.readlines()

    times = list(map(int,data[0].strip().split()[1:]))
    distances = list(map(int,data[1].strip().split()[1:]))

    print(times)
    print(distances)
    return times,distances

def part1():
    answers = []
    print(times)
    for x in range(0,len(times)):
        count = 0
        for n in range(1,times[x]):
            distance = ((times[x]-n)*n)
            print(distance)
            if distance > distances[x]:
                count += 1
        answers.append(count)
    print(math.prod(answers))


times,distances = process('6.in')
part1()

