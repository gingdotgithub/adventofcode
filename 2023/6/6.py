import math

distances = []
times = []

def process(filename):
    with open(filename) as f:
        data = f.readlines()

    #part 1
    # times = list(map(int,data[0].strip().split()[1:]))
    # distances = list(map(int,data[1].strip().split()[1:]))
    #part 2
    times.append(int(''.join(data[0].strip().split()[1:])))
    distances.append(int(''.join(data[1].strip().split()[1:])))

    print(times)
    print(distances)
    return times,distances

def part1():
    answers = []
    for x in range(0,len(times)):
        count = 0
        for n in range(1,times[x]):
            distance = ((times[x]-n)*n)
            #print(distance)
            if distance > distances[x]:
                count += 1
        answers.append(count)
    print("answer:",math.prod(answers))


times,distances = process('6.in')
part1() 
#part 2 see changes in processing

