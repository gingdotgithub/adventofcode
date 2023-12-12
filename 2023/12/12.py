#done with thanks to some learning by watching https://www.youtube.com/watch?v=g3Ms5e7Jdqo
#some of the following is more long form, but its to make more sense for my own learning. 
import time

with open('12.in') as f:
    data = f.readlines()
starttime = time.time()

cache = {} #for part 2

def search(pattern,nums):
    #if there are no more pattern and we have no more groups to find, then thats the correct end state, so we return 1
    #else we return 0 because thats not a valid state to be in
    #basically if we got to the end of the pattern and theres nothing else to find. thats good.
    if pattern == "": 
        if nums == ():
            return 1
        else:
            return 0

    #if there are no more numbers to process and no more hashes in the pattner, thats good, return 1
    #else we return 0 because there are more hashes that need filling
    #basically... if theres nothing left to find, but theres still pattern, its good as long as theres no more # in it
    if nums == ():
        if "#" not in pattern:
            return 1
        else:
            return 0

    #otherwise, we have pattern left to process. that could have multiple good states
    states = 0

    #for the sake of part 2, we'll save time by putting anything we've checked before in a cache. 
    #so first things first, if its already in the cache, we can just return that. and if not, we'll calc it after and store it.
    cacheitem = (pattern,nums)
    if cacheitem in cache:
        return cache[cacheitem]

    #if we find an operational spring, or one that could be (a ?), then take it off and keep checking and we'll add anything we find
    if pattern[0] == "." or pattern[0] == "?":
        states += search(pattern[1:], nums) 

    #if we find the beginning of a group, or one that could be (a ?), then lets process it as a group, take it out, and check down the line after that with the remaining nums
    if pattern[0] == "#" or pattern[0] == "?":
        if len(pattern) >= nums[0]: #ie theres enough chars left to form a group this size
            if "." not in pattern[0:nums[0]]: #ie theres definitely no operational springs (could be # or ?) for the next n parts
                if len(pattern) == nums[0]: #if the group we found gets to the of the line:
                    states += search(pattern[nums[0]:], nums[1:]) #take the group off and take a group-to-find off - since this is the end, the next recursion down should return a 1 for getting to the end correctly
                elif (pattern[nums[0]] == "." or pattern[nums[0]] == "?"): # or ie the group then ends (a .) or could end (a ?)
                    #ie at this point we have found a valid set of # (or ?s) that is long enough and theres a possible dot after it.
                    states += search(pattern[nums[0]+1:], nums[1:]) #take off the group and the next operational one, and remove a group-to-find. 

    #in the code above a . is treated as definitely an operational spring. a # is broken spring. and a ? is run in both to see whether they lead to valid states

    #this will now be the number of subsequent states found that are valid. 
    #for part 2, we'll put it in a cache so we can cut down time. 
    cache[cacheitem] = states
    return states
    
        

answer = 0
for line in data:
    pattern,nums = line.strip().split()
    nums = tuple(map(int,nums.split(",")))
    print(pattern,nums)
    answer += search(pattern,nums)

endtime = time.time()
print("part 1:",answer)
print("timing:",endtime-starttime)

starttime = time.time()
answer = 0
for line in data:
    pattern,nums = line.strip().split()
    nums = tuple(map(int,nums.split(",")))
    newpattern = pattern
    newnums = nums
    for x in range(0,4):
        newpattern = newpattern+"?"+pattern
        newnums += nums
    print(newnums)
    print(newpattern,newnums)
    answer+= search(newpattern,newnums)

endtime = time.time()
print("part 2:",answer)
print("timing:",endtime-starttime)