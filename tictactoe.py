from random import randint
import time

#@Ned Hulseman
#@Thursday, October 3 2017
#


     
#function used to enter in player types at the beginning of the game
#Options are human, robot or dumb robot
#if an incorrect string is input, then it will give another prompt for an input
def playerType(p): #@param p for player 1 or 2
    player=""
    while player != "r sammy" and player != "chetter hummin" and player!="dumb robot":
        player=input("Is player " + str(p) + " a human, Chetter Hummin or R Sammy?")
        player=player.lower()
        if player != "r sammy" and player != "human" and player!="chetter hummin":
            print("Failure is not an option, and neither is your input. Try again cowboy")
    return player


#Function to show how the board is layed out
def instructionalBoard():
    print ("This is how the board is layed out")
    print("-------")
    print("|1|2|3|")
    print("-------")
    print("|4|5|6|")
    print("-------")
    print("|7|8|9|")
    print("-------")
#Function is used to update the list board    
def update(board, move, letter): # @param list board, @param int move, @param char letter to denote X or Y 
    move=int(move)
    board[move]=letter
    return board

#function to print board
def printBoard(board):#@param list board
    print("-------")
    print("|" + board[0] +"|" + board[1] + "|" + board[2] + "|")
    print("-------")
    print("|" + board[3] +"|" + board[4] + "|" + board[5] + "|")
    print("-------")
    print("|" + board[6] +"|" + board[7] + "|" + board[8] + "|")
    print("-------")
 
#function to call for a humanMove()
#this function does not allow moves that are out of bounds
#or a player to overwrite a space that has already been taken
def humanMove(*board):#@param list board
    move=0
    track=False
    while track==False:
        move=int(input("Please enter a move"))
        if move>0 and move<10:
            if board[move-1]==" ":
                track=True
            else:
              print("That space is taken")  
        else:
            print("I do believe you entered in the wrong number")
    move-=1
    return move

#function to call on dumb robot
#selects random numbers between 0 and 8 iunclusive
#until it chooses a space that has not been taken  
def dumbRobotMove(*board):#@param list board
    move=0
    track=False
    while track==False:
        move=randint(0, 8)
        if board[move]==" ":
            track=True
    return move
#returns the space that the robot should go
def smartRobot(*board, letter, opponentLetter):
    rule=False
    #Rule 1
    if letter not in board:#if first move take a corner that is not taken
        corners=[0, 2, 6, 8]
        move=int(randint(0, 3))
        if board[corners[move]]!=" ":
            while board[corners[move]]!=" ":
                move=randint(0, 3)
        rule=True
        return corners[move] 
    #Rule 2
    if rule==False:
        j=0
        board=list(board)
        for i in board:#checks if robot has any winning moves
            if rule==False:
                if board[j]==" ":
                    board[j]=letter
                    if checkWinner(board)==True:
                        rule=True
                        return j
                    else:
                        board[j]=" "
            j+=1
    #Rule 3
    if rule==False:#check if opponent has any winning moves
        j=0
        board=list(board)
        for i in board:
            if rule==False:
                if board[j]==" ":
                    board[j]=opponentLetter
                    if checkWinner(board)==True:
                        rule=True
                        return j
                    else:
                        board[j]=" "
            j+=1
    #Rule 4
    if rule==False:#take another open corner
        corners=[0,2,6,8]
        openCorner=[False, False, False, False]
        if board[0]==" ":
            openCorner[0]=True
        if board[2]==" ":
            openCorner[1]=True
        if board[6]==" ":
            openCorner[2]=True
        if board[8]==" ":
            openCorner[3]=True
        if True in openCorner:
            while rule==False:
                move=randint(0,3)
                if openCorner[move]==True:
                    rule=True
                    return corners[move]
    #Rule 5
    if rule==False:
        print("rule 5")
        rule=True
        return dumbRobotMove(*board)
#smart robot
#function that keeps all possible 2 in a row combinations for first rule
#rule four corners
def winningMove(*board, letter):
    if board[0]==letter and board[1]==letter and board[2]==" ":
        return 2 
    elif board[0]==letter and board[2]==letter and board[1]==" ":
        return 1 
    elif board[1]==letter and board[2]==letter and board[0]==" ":
        return 0 
    elif board[3]==letter and board[4]==letter and board[5]==" ":
        return 6
    elif board[3]==letter and board[5]==letter and board[4]==" ":
        return 4  
    elif board[4]==letter and board[5]==letter and board[3]==" ":
        return 3   
    elif board[6]==letter and board[7]==letter and board[8]==" ":
        return 8
    elif board[6]==letter and board[8]==letter and board[7]==" ":
        return 7  
    elif board[4]==letter and board[5]==letter and board[3]==" ":
        return 3 
#def smartRobot(*board):
    

#checks all possible ways a player could win     
def checkWinner(board):#@param list board
    if board[0]==board[1]==board[2] and board[0]!=' ':
        return True 
    elif board[3]==board[4]==board[5] and board[3]!=' ':
        return True 
    elif board[6]==board[7]==board[8] and board[6]!=' ':
        return True 
    elif board[0]==board[4]==board[8] and board[0]!=' ':
        return True 
    elif board[2]==board[4]==board[6] and board[2]!=' ':
        return True 
    elif board[0]==board[3]==board[6] and board[0]!=' ':
        return True 
    elif board[1]==board[4]==board[7] and board[1]!=' ':
        return True 
    elif board[2]==board[5]==board[8] and board[2]!=' ':
        return True 
    else:
        return False

#checks to see if there is a cats game
def checkCatsGame(board):#@param list board
    if " " in board:
        return False
    else:
        return True
   
    

     
#gameplay
print("Hello and welcome to Ned's wonderful Tic Tac Toe")
play1=str(1)
play2=str(2)

player1=playerType(play1)
player2=playerType(play2)
board=[" ", " ", " ", " "," ", " "," ", " ", " "]  
playerWin=0
catsGame=False
winner=False

instructionalBoard()
printBoard(board)

while catsGame==False and winner==False:
    if player1=="human":
        turn=humanMove(*board)
    elif player1=="r sammy":
        time.sleep(2)
        turn=dumbRobotMove(*board)
    elif player1=="chetter hummin":
        time.sleep(2)
        turn=smartRobot(*board, letter='X', opponentLetter='O')
    board=update(board, turn, 'X')
    printBoard(board)
    catsGame=checkCatsGame(board)
    winner=checkWinner(board)
    if winner:
        playerWin=1
    if catsGame==False and winner==False:
        if player2=="human":
            turn=humanMove(*board)
        elif player2=="r sammy":
            time.sleep(2)
            turn=dumbRobotMove(*board)
        elif player2=="chetter hummin":
            time.sleep(2)
            turn=smartRobot(*board, letter="O", opponentLetter="X")
        board=update(board, turn, 'O')
        printBoard(board)
        winner=checkWinner(board) 
        if winner:
            playerWin=2
    catsGame=checkCatsGame(board)

if winner:
    print("Player " + str(playerWin) + " wins!")     
else:
    print("Cats Game")

        
        
        
        
        
        
    













