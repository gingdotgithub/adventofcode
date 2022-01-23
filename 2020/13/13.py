starttime = 1005526
busses = [37,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',41,'x','x','x','x','x','x','x','x','x',587,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',13,19,'x','x','x',23,'x','x','x','x','x',29,'x',733,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',17]
# starttime = 939
# busses = [7,13,'x','x',59,'x',31,19]
notfound = True

timestamp = starttime
while notfound:
    timestamp += 1
    for bus in busses:
        if bus != 'x':
            if timestamp % int(bus) == 0:
                print(str(timestamp) + " - " + str(bus) + " - " + str((timestamp-starttime)*bus))
                notfound = False
                break

