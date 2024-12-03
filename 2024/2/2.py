with open('2.in') as f:
    dataset = f.readlines()

safereports = 0
for line in dataset:
    originalreport = [int(x) for x in line.split()]
    print(originalreport)
    #check data

    remover = -1

    while remover < len(originalreport):
        report = originalreport[:]
        if remover >= 0:
            del report[remover]
        print("trying ",report)
    
        issafe = True
        xdiffdir = 0

        x = 1
        while issafe and x < len(report):
            xdiff = report[x] - report[x-1]

            if abs(xdiff) < 1 or abs(xdiff) > 3:
                issafe = False
                # break

            if xdiffdir == 0:
                if xdiff < 0:
                    xdiffdir = -1
                elif xdiff > 0:
                    xdiffdir = 1
            
            if (xdiff < 0 and xdiffdir > 0) or (xdiff > 0 and xdiffdir < 0):
                issafe = False
                # break

            x+=1

        if issafe:
            safereports += 1
            print("safe!!!!!")
            break
        else:
            print("not safe")
            remover += 1
        
    


print(safereports)