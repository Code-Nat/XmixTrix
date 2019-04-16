
from getpass import getpass

def DisplayTable (GameTable):
    print ("-"*13)
    for i in GameTable:
        for j in i:
            print ("|", j, end = " ")
        print ("|")
        print ("-"*13)

def DisplayScore(X,O):
    print ("Score:\n X player: | O player:")
    print (" "*3,X," "*4,"|"," "*3,O)

def testInpurt ():
    i = input ("Please enter a location from 1 to 9:")
    while (i > "9" or i < "1") or len(i)!=1:
        i = input ("The number you have entered is unvalid, please enter a number from 1 to 9:")
    return int(i)

def winnerTest(GameTable):
    for i in range (0,3):
        if (GameTable[0][i] == GameTable[1][i]):
            if (GameTable[0][i] == GameTable[2][i]):
                return True
        if (GameTable[i][0] == GameTable[i][1]):
            if (GameTable[i][0] == GameTable[i][2]):
                return True
    if (GameTable[0][2] == GameTable[1][1]):
            if (GameTable[2][0] == GameTable[1][1]):
                return True
    if (GameTable[0][0] == GameTable[1][1]):
        if (GameTable[2][2] == GameTable[1][1]):
            return True
    return False

X = 0
O = 0

while True:
    GameTable = [[1,2,3],[4,5,6],[7,8,9]]

    for turn in range (0,9):
        DisplayTable (GameTable)
        
        place = testInpurt()-1
        while (GameTable[int(place/3)][place%3] == "X" or GameTable[int(place/3)][place%3] == "O"):
            print ("The location you have entered is all ready taken")
            DisplayTable(GameTable)
            place = testInpurt()-1
        else:
            if (turn%2 == 0):
                GameTable[int(place/3)][place%3] = "X"
            else:
                GameTable[int(place/3)][place%3] = "O"

        if winnerTest(GameTable):
            break
    
    else:
        print ("Its a tie")
        DisplayTable (GameTable)
        DisplayScore(X,O)
        continue
    
    DisplayTable(GameTable)

    if (turn%2 == 0):
        print ("X is the winner")
        X += 1
    else:
        print ("O is the winner")
        O += 1
    
    DisplayScore(X,O)

    if (getpass("Press Enter to play again, press Q then enter").lower() == "q"):
        break
        
        

