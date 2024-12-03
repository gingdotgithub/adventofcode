import re

with open('3.in') as f:
    dataset = f.readlines()

result = 0
doing = True
for line in dataset:
    answers = re.findall('(do\(\)|don\'t\(\)|mul\(\d+,\d+\))',line)
    print(answers)
    for answer in answers:
        if answer == "do()":
            doing = True
            continue
        if answer == "don't()":
            doing = False
            continue
        else:
            if doing:
                nums = re.findall("\d+",answer)
                print(nums)
                result = result + (int(nums[0]) * int(nums[1]))

print(result)