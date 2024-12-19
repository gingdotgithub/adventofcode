import time
import functools

with open('19.in') as f:
    dataset = f.readlines()
    dataset = [line.rstrip('\n') for line in dataset]

stripes = dataset.pop(0).split(", ")
dataset.pop(0)
# print(strips)
# print(dataset)

@functools.cache
def cansolve(target):
    global stripes
    for stripe in stripes:
        print("trying",stripe)
        if stripe == target:
            print("found mathcing end",stripe,target)
            return True
        if target[:len(stripe)] == stripe:
            print("found",stripe,"checking",target[len(stripe):])
            if cansolve(target[len(stripe):]):
                return True
    return False

count = 0
for target in dataset:
    print("TARGET IS",target)
    if cansolve(target):
        count+=1
        print("count is now",count)
        # temp = input()

time2 = time.time()
print("Part 1:",count)

