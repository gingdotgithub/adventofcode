import re

def process(filename):
    with open(filename) as f:
        dataset = f.readlines()

    output = 0
    for line in dataset:
        numbers = re.sub("[^0-9]","",line)
        calibration = str(numbers[0]) + str(numbers[len(numbers)-1])
        output = output + int(calibration)
    return output


def test():
    print("test answer is:",process('1.test'))

def part1():
    print("part 1:",process('1.in'))

test()
part1()