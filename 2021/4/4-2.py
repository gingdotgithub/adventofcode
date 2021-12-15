inputs = input().split(',')
newline = input()
#board = [score,0score,inputid,row1,row2,row3,row4,row5,col1,col2,col3,col4,col5]
boards = []

while True:
    newline = input()
    if newline == '':
        break
    board = [0]*13
    for x in range(5):
        row = newline.split()
        for y in range(5):
            if row[y] in inputs:
                board[0]+=inputs.index(row[y])
                board[2+x]+=1
                board[7+y]+=1
            else:
                board[1]+=int(row[y])
        newline = input()
    newline = input()