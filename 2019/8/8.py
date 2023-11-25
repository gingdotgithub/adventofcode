
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
    print(onecount*twocount)

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