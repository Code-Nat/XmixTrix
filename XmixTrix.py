
from getpass import getpass #Inport for password function to be able to reqrest text without display
##############################################################Functions for software#################################################
def DisplayTable (GameTable): #Function to print the table
    print ("-"*13)
    for i in GameTable:
        for j in i:
            print ("|", j, end = " ")
        print ("|")
        print ("-"*13)

def DisplayScore(X,O): #Function to print the scores
    print ("Score:\n X player: | O player:")
    print (" "*3,X," "*4,"|"," "*3,O)

def testInpurt (): #Function for reciving input from user and verfiying the input is valid
    i = input ("Please enter a location from 1 to 9:")
    while (i > "9" or i < "1") or len(i)!=1:
        i = input ("The number you have entered is unvalid, please enter a number from 1 to 9:")
    return int(i)

def winnerTest(GameTable): #Functrion to test if anyone won the game
    for i in range (0,3): #Testing lines
        if (GameTable[0][i] == GameTable[1][i]):
            if (GameTable[0][i] == GameTable[2][i]):
                return True
        if (GameTable[i][0] == GameTable[i][1]):
            if (GameTable[i][0] == GameTable[i][2]):
                return True
    if (GameTable[0][2] == GameTable[1][1]): #Testing Axsis
            if (GameTable[2][0] == GameTable[1][1]):
                return True
    if (GameTable[0][0] == GameTable[1][1]):
        if (GameTable[2][2] == GameTable[1][1]):
            return True
    return False
##################################### End if function area #################################################
X = 0 #Zero Scores
O = 0
################# From this point start game code ######################################
while True: 
    GameTable = [[1,2,3],[4,5,6],[7,8,9]] #Clean the game boerd

    for turn in range (0,9): ########################## Function for turns runs from one to 9 (max) turns
        DisplayTable (GameTable)
        
        place = testInpurt()-1 #Get valid input form user take down one for lateler cal
        while (GameTable[int(place/3)][place%3] == "X" or GameTable[int(place/3)][place%3] == "O"): #Verfiy not in ocupied spot
            print ("The location you have entered is all ready taken")
            DisplayTable(GameTable)
            place = testInpurt()-1
        else: ################################# X has the Even turns O has the odd turns
            if (turn%2 == 0):
                GameTable[int(place/3)][place%3] = "X"
            else:
                GameTable[int(place/3)][place%3] = "O"

        if winnerTest(GameTable): ####### If someone won quit
            break
    
    else: # If the turn loop run for 9 rounds its a tie
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

    if (getpass("Press Enter to play again, press Q then enter").lower() == "q"): # Recive input without showing to user using getpass that is made for passwords
        break
        
        

