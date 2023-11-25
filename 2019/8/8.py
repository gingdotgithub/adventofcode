
def part1():
    mostzerolayer = ""
    mostzeros = 150
    for layerdata in imagegrid:
        zerocount = layerdata.count("0")
        if zerocount < mostzeros:
            mostzeros = zerocount
            mostzerolayer = layerdata

    onecount = mostzerolayer.count("1")
    twocount = mostzerolayer.count("2")
    print("part 1 answer: ", onecount*twocount)

def part2():
     answer = ""
     for y in range(0,height):
        for x in range(0,width):
             for i in range(0,len(imagegrid)):
                  if imagegrid[i][(width*y)+x] == "0":
                       answer = answer + " "
                       break
                  elif imagegrid[i][(width*y)+x] == "1":
                       answer = answer + "0"
                       break
        answer = answer + "\n"
     print("part 2 answer: \n")
     print(answer)
          

imagedata = ""
imagegrid = []
width = 25
height = 6
with open('8.in') as f:
        imagedata= f.readline()
x = 0
layer = width*height
while x < len(imagedata):
    imagegrid.append(imagedata[x:x+layer])
    x = x+layer

part1()
part2()