import time
import random

data = open('25.in').read().splitlines()
starttime = time.time()

graph = {}
edges = []

def buildGraph():
    for line in data:
        node,neighbours = line.split(": ")
        if node not in graph:
            graph[(node)] = set()
        neighbours = neighbours.split(" ")
        for n in neighbours:
            if n not in graph:
                graph[(n)] = set()
            graph[(node)].add(n)
            graph[(n)].add(node)
            edges.append((min(node,n),max(node,n)))

def printGraph():
    for node in graph:
        print(node,graph[node])

def countNodes():
    return len(graph)

def countEdges():
    count = 0
    for node in graph:
        count+=len(graph[node])
    return count

def karger():
    count = 0
    while True: 
        count+=1
        #print("doing karger ",count)
        #do karger algo
        cuts = []
        thisg = graph.copy()
        thise = edges.copy()
        while len(thisg) > 2:
            e = random.choice(thise)
            #print("e is",e)
            thise.remove(e)
            sn0 = e[0] #need to find the supernode of e[0]
            sn1 = e[1] #need to find the supernode of e[1]
            for snkey in thisg:
                if sn0 in snkey:
                    sn0 = snkey
                if sn1 in snkey:
                    sn1 = snkey
            if sn1 == sn0:
                continue
            #print(sn0,sn1)            
            seta = thisg[sn0] 
            setb = thisg[sn1] 
            thisg.pop(sn0)
            thisg.pop(sn1)
            if isinstance(sn0,str):
                sn0 = {sn0}
            else:
                sn0 = set(sn0)
            if isinstance(sn1,str):
                sn1 = {sn1}
            else:
                sn1 = set(sn1)
            seta = seta-sn1
            setb = setb-sn0
            e = tuple(sn0 | sn1)
            #print(e)
            thisg[e] = seta | setb
            #print(e,"is",thisg[e])
            #print(thisg)
            #print(thise)
            #f = input("?")
        #print("got it down to two")#,thisg)
        #f = input("?")
        

        if len(thisg[list(thisg.keys())[0]]) == 3:
            print("found on karger round",count)
            return thisg.keys()

buildGraph()
#printGraph()
#print(edges)
#print(countNodes(),"nodes and",countEdges(),"edges")

cuts = list(karger())
#print(cuts)
print("part 1",len(cuts[0])*len(cuts[1]))
print("timing:",time.time()-starttime)