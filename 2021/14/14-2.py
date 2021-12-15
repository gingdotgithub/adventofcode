from collections import defaultdict

startingcode = input() #the given polymer
reference = {} #the reference list provided
lettercounts = defaultdict(int) #count of individual letters
paircounts = defaultdict(int) #counts of pairs being created

input() #read the blank line
#read in the reference list for use
while True:
    newline = input()
    if newline == '':
        break
    parts = newline.split(' -> ')
    reference[parts[0]] = parts[1]

#process the polymer - create a count of the letters in it, and the pairs
for i in range(len(startingcode)-1):
    lettercounts[startingcode[i:i+1]]+=1
    paircounts[startingcode[i:i+2]]+=1
n = len(startingcode) #its a bit painful to get the last letter without the i+2 going over ^^
lettercounts[startingcode[n-1:n]]+=1

#these are the steps of increment
for i in range(40):
    #grab a copy of the current pair counts, and cycle through them
    #get the new letter from the reference
    #since we are going to do the same to all N of that pair
    #we will add N more of the new letter
    #and create N more of the new left pairing and new right pairing
    #and remove N of the pair we had
    for pair, countofpair in paircounts.copy().items():
        lettertoadd = reference[pair]
        lettercounts[lettertoadd]+=countofpair
        paircounts[pair[0]+lettertoadd]+=countofpair
        paircounts[lettertoadd+pair[1]]+=countofpair
        paircounts[pair]-=countofpair

print(str(max(lettercounts.values()) - min(lettercounts.values())))