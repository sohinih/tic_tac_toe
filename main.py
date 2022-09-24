def printBoard():
    one='X' if xState[0] else ('O' if yState[0] else ' ')
    two='X' if xState[1] else ('O' if yState[1] else ' ')
    three ='X' if xState[2] else ('O' if yState[2] else ' ')
    four = 'X' if xState[3] else ('O' if yState[3] else ' ')
    five = 'X' if xState[4] else ('O' if yState[4] else ' ')
    six = 'X' if xState[5] else ('O' if yState[5] else ' ')
    seven = 'X' if xState[6] else ('O' if yState[6] else ' ')
    eight = 'X' if xState[7] else ('O' if yState[7] else ' ')
    nine = 'X' if xState[8] else ('O' if yState[8] else ' ')
    print(f"{one}  | {two}  | {three} ")
    print("---|----|---")
    print(f"{four}  | {five}  | {six} ")
    print("---|----|---")
    print(f"{seven}  | {eight}  | {nine} ")

def sum(a,b,c):
    return a+b+c

def check(xState,yState):
    wins=[[0,1,2],[0,3,6],[3,4,5],[6,7,8],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for item in wins:
        if (sum(xState[item[0]], xState[item[1]], xState[item[2]])==3):
            return 1
        if (sum(yState[item[0]], yState[item[1]], yState[item[2]]) == 3):
            return 0
    return -1

xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print("WELCOME TO TIC TAC TOE\n")
turn=1
printBoard()
count=0
while(True):
    if(turn==1):
        print("PLAYER 1's chance")
        value=int(input("Enter a position (from 0 to 9) to put X mark : "))
        while(value>9 or value<0):
            print("WRONG INPUT\nEnter your choice again : ")
            value = int(input("Enter a position (from 0 to 9) to put X mark : "))
            if(value>=0 and value<=9):
                break
        xState[value-1]=1
        turn=0
        count=count+1
    else:
        print("PLAYER 2's chance")
        value = int(input("Enter a position (from 1 to 9) to put 0 mark : "))
        while (value > 9 or value < 0):
            print("WRONG INPUT\nEnter your choice again : ")
            value = int(input("Enter a position (from 1 to 9) to put X mark : "))
            if (value >= 0 and value <= 9):
                break
        yState[value-1] = 1
        turn=1
        count = count + 1
    printBoard()
    z = check(xState,yState)
    if (z != -1):
        if(z==1):
            print("PLAYER 1 WINS")
        else:
            print("PLAYER 2 WINS")
        break
    if (count==9):
        print("Match over and no one wins ")
        break