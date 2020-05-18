import random
import copy

print("Welcome to 2048!")
n=int(input("Enter grid size"))

board=[]
for i in range(n):

    row=[]
    for j in range(n):
        row.append(0)
    board.append(row)

def newvalue():
    if random.randint(1,8)==1:
        return 4
    else:
        return 2


startnum = 2
while startnum > 0:
    rowNum = random.randint(0, n - 1)
    colNum = random.randint(0, n- 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = newvalue()
        startnum -= 1

def display():
    for row in board:
        curRow="|"
        for element in row:
            if element==0:
                curRow+="    |"
            else:
                curRow+=str(element)+((4-len(str(element)))*" ")+"|"
        print(curRow)
    print()
display()

def mergeOneRowL(row):
    for j in range(n-1):
        for i in range(n-1,0,-1):
            if row[i-1]==0:
                row[i-1]=row[i]
                row[i]=0
    for i in range(n-1):
        if row[i]==row[i+1]:
            row[i]*=2
            row[i+1]=0
    for i in range(n-1,0,-1):
        if row[i-1]==0:
            row[i-1]=row[i]
            row[i]=0
    return row

def merge_left(currentboard):
    for i in range(n):
        currentboard[i]=mergeOneRowL(currentboard[i])
    return currentboard

def revese(row):
    newboard=[]
    for i in range(n-1,-1,-1):
        newboard.append(row[i])
    return newboard

def merge_right(currentboard):
    for i in range(n):
        currentboard[i]=revese(currentboard[i])
        currentboard[i]=mergeOneRowL(currentboard[i])
        currentboard[i]=revese(currentboard[i])
    return currentboard

def transpose(currentboard):
    for j in range(n):
        for i in range(j,n):
            if not i==j:
                temp=currentboard[j][i]
                currentboard[j][i]=currentboard[i][j]
                currentboard[i][j]=temp
    return currentboard

def merge_up(currentboard):
    currentboard = transpose(currentboard)
    currentboard = merge_left(currentboard)
    currentboard = transpose(currentboard)

    return currentboard
def merge_down(currentboard):
    currentboard = transpose(currentboard)
    currentboard = merge_right(currentboard)
    currentboard = transpose(currentboard)

    return currentboard



def addnewValue():
    rowNum=random.randint(0,n-1)
    colNum=random.randint(0,n-1)

    while not board[rowNum][colNum]==0:
        rowNum=random.randint(0,n-1)
        colNum=random.randint(0,n-1)

    board[rowNum][colNum]=newvalue()



def won():
    for row in board:
        if 2048 in row:
            return True
    return False

def noMoves():
    tempboard1=copy.deepcopy(board)
    tempboard2=copy.deepcopy(board)

    tempboard1=merge_down(tempboard1)
    if tempboard1==tempboard2:
        tempboard1=merge_up(tempboard1)
        if tempboard1==tempboard2:
            tempboard1=merge_right(tempboard1)
            if tempboard1==tempboard2:
                tempboard1=merge_left(tempboard1)
                if tempboard1==tempboard2:
                    return True
    return False


gameOver=False

while not gameOver:
    move=[0]
    move=input("which way to merge?")

    validInput=True

    tempboard=copy.deepcopy(board)

    if move=="d":
        board=merge_right(board)
    elif move=="w":
        board=merge_up(board)
    elif move=="a":
        board=merge_left(board)
    elif move=="s":
        board=merge_down(board)
    else:
         validInput=False

    if not validInput:

        print("your input was not valid,try again")
    else:
        if board==tempboard:

            print("Try different direction!")
        if won():
            print("You Won!")
            gameOver = True


        if noMoves():
            print("no more moves left.GAME OVER.")
            gameOver = True
            display()

        else:

            addnewValue()
            display()