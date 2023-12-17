import heapq
import time

data = open('17.in').read().splitlines()
starttime = time.time()

seen = set() #for states been to already
queue = [] #for the priority queue
start = (0,0,(0,0),(1,0),0) #heuristic, heat loss, (x, y), (dirX, dirY), steps
    #heuristic in this case is for a* rather than dijkstra
target = (len(data)-1,len(data[0])-1)
heapq.heappush(queue,start)
    #in tihs case the objects in the queue include the heuristic, the increasing heatloss, the location, the direction, and the number of steps taken

while len(queue) > 0:
    heur, heatloss, coord, dir, steps = heapq.heappop(queue)

    if coord == target: #this is if... its found the target. 
        endtime = time.time()
        print("part 1:", heatloss)
        print("timing:",endtime-starttime)
        break

    if (coord,dir,steps) not in seen:
        seen.add((coord,dir,steps)) #seen is tracking location, directiona, and steps, because if its just location, then it doesnt keep track of routes
                                    #that were valid and equally weighted, before rejecting them entirely because the wrong way there later broke the 3 step rule
                                    #so its got to track every path its taking, not every node its got to. 

        if steps < 3: #assuming its trying to go in the same direction - can it still?
            nextcoord = (coord[0]+dir[0],coord[1]+dir[1])
            if nextcoord[0] >= 0 and nextcoord[0] < len(data[0]) and nextcoord[1] >= 0 and nextcoord[1] < len(data): #still inside grid
                newheatloss = heatloss+int(data[nextcoord[1]][nextcoord[0]]) #standard dikstra cost add
                heuristic = newheatloss+((target[0]-nextcoord[0])+(target[1]-nextcoord[1])) #a* heuristic using manhattan distance
                heapq.heappush(queue,(heuristic,newheatloss,nextcoord,dir,steps+1)) #add to the heapqueue
        
        directions = [(1,0),(0,-1),(-1,0),(0,1)] #these are all possible directions
        for newdir in directions: #we're looking for left and right
            if newdir != dir and newdir != (-dir[0],-dir[1]): #so same as dir is forward, and reverse of dir is backward
                nextcoord = (coord[0]+newdir[0],coord[1]+newdir[1]) #same as above
                if nextcoord[0] >= 0 and nextcoord[0] < len(data[0]) and nextcoord[1] >= 0 and nextcoord[1] < len(data):
                    newheatloss = heatloss+int(data[nextcoord[1]][nextcoord[0]])
                    heuristic = newheatloss+((target[0]-nextcoord[0])+(target[1]-nextcoord[1]))
                    heapq.heappush(queue,(heuristic,newheatloss,nextcoord,newdir,1))
    
