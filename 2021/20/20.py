image0 = []
image1 = []
image2 = []
image3 = []

######## read in
enhancealgo = input()
input()
while True:
    newline = input()
    if newline == '':
        break
    image0.append(list(newline))

def convert_to_binary(pixel):
    pixelbinary = ''
    for x in range(len(pixel)):
        pixelbinary += "0" if pixel[x:x+1] == '.' else "1"
    return pixelbinary

def expandimage(imagev1, imagev2, expandchar):
    imagev2.append([expandchar]*(len(imagev1[0])+4))
    imagev2.append([expandchar]*(len(imagev1[0])+4))
    for row in imagev1:
        newrow = [expandchar,expandchar]
        for item in row:
            newrow.append(item)
        newrow.append(expandchar)
        newrow.append(expandchar)
        imagev2.append(newrow)
    imagev2.append([expandchar]*(len(imagev1[0])+4))
    imagev2.append([expandchar]*(len(imagev1[0])+4))
    for row in imagev2:
        print("".join(row))
    print("")

def enhanceimage(imagev1, imagev2, expandchar):
    for x in range(-2,len(imagev1[0])+2):
        for y in range(-2, len(imagev1)+2):
            pixel = ''
            pixel+= imagev1[y-1][x-1] if 0 <= (x-1) < len(imagev1[0]) and 0 <= (y-1) < len(imagev1) else expandchar
            pixel+= imagev1[y-1][x] if 0 <= x < len(imagev1[0]) and 0 <= (y-1) < len(imagev1) else expandchar
            pixel+= imagev1[y-1][x+1] if 0 <= (x+1) < len(imagev1[0]) and 0 <= (y-1) < len(imagev1) else expandchar
            pixel+= imagev1[y][x-1] if 0 <= (x-1) < len(imagev1[0]) and 0 <= (y) < len(imagev1) else expandchar
            pixel+= imagev1[y][x] if 0 <= x < len(imagev1[0]) and 0 <= (y) < len(imagev1) else expandchar
            pixel+= imagev1[y][x+1] if 0 <= (x+1) < len(imagev1[0]) and 0 <= (y) < len(imagev1) else expandchar
            pixel+= imagev1[y+1][x-1] if 0 <= (x-1) < len(imagev1[0]) and 0 <= (y+1) < len(imagev1) else expandchar
            pixel+= imagev1[y+1][x] if 0 <= x < len(imagev1[0]) and 0 <= (y+1) < len(imagev1) else expandchar
            pixel+= imagev1[y+1][x+1] if 0 <= (x+1) < len(imagev1[0]) and 0 <= (y+1) < len(imagev1) else expandchar
            pixelbinary = convert_to_binary(pixel)
            result = enhancealgo[int(pixelbinary,2)]
            imagev2[y+2][x+2] = result

    for row in imagev2:
        print("".join(row))
    print("")

expandimage(image0, image1,'.')
# expandimage(image1, image2, '.')
# enhanceimage(image1, image2, '.')
# expandimage(image2, image3, image2[0][0])
# enhanceimage(image2,image3, image2[0][0])

for x in range(50):
    expandimage(image1, image2, image1[0][0])
    enhanceimage(image1, image2, image1[0][0])
    image1 = image2.copy()
    image2 = []

countoflit = sum(x.count('#') for x in image1)
print(countoflit)