import random

'''
Parques numbers spaces meanings
The track is the index of every tile in a simulated parques board on a four-person board with red on the bottom right corner, green on the top right, blue on the top left, and yellow on the bottom left
track = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104]
1-68 : Main track counterclockwise from red start to behind red start
1,18,35,52 : Starting tiles for the pieces
8,13,25,30,42,47,59,64 : Protected tiles
69-76 : Red safe zone
77-84: Green safe zone
85-92: Blue safe zone 
93-100: Yellow safe zone 
101: Red Jail
102: Green Jail
103: Blue Jail
104: Yellow Jail


 The following four classes are the four different colors of pieces used in this simulation of parques.
    The track is the path that it will take in order, from beginning to end. 
    The index is the current position of that piece along its track.
    The following parameters are parts of the status of a piece
    -   inJail is whether or not a piece is in its Jail
    -   done is whether or not a piece is finished/off the board
    -   closeMove is whether or not a piece is too close to the finishing tile to move
    -   closeDice1 is whether or not the value of Dice1 is greater than the amount of spaces the piece is from the finishing tile
    -   closeDice2 is whether or not the value of Dice2 is greater than the amount of spaces the piece is from the finishing tile
    -   closeDice1 is whether or not the combined value of the dice is greater than the amount of spaces the piece is from the finishing tile
'''
class redPiece:
    def __init__(self):
       self.index = 0
       self.track = [101,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,69,70,71,72,73,74,75,76]
       self.inJail = True
       self.done = False
       self.closeMove = False
       self.closeDice1 = False
       self.closeDice2 = False
       self.closeCombined = False

class greenPiece:
    def __init__(self):
       self.index = 0
       self.track = [102,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,1,2,3,4,5,6,7,8,9,10,11,12,13,77,78,79,80,81,82,83,84]
       self.inJail = True
       self.done = False
       self.closeMove = False
       self.closeDice1 = False
       self.closeDice2 = False
       self.closeCombined = False
       
class bluePiece:
    def __init__(self):
       self.index = 0
       self.track = [103,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,85,86,87,88,89,90,91,92]
       self.inJail = True
       self.done = False
       self.closeMove = False
       self.closeDice1 = False
       self.closeDice2 = False
       self.closeCombined = False

class yellowPiece:
    def __init__(self):
       self.index = 0
       self.track = [104,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,93,94,95,96,97,98,99,100]
       self.inJail = True
       self.done = False
       self.closeMove = False
       self.closeDice1 = False
       self.closeDice2 = False
       self.closeCombined = False

#Used at the beginning of a move to update the status of a piece based solely on its index
def status(piece):
    if piece.index == 0:
        piece.inJail = True

    else:
        piece.inJail = False 

    if piece.index == 72:
        piece.done = True

    else:
        piece.done = False

#Repeats the status method for every piece of a color
def statusAll(piece1,piece2,piece3,piece4):
    status(piece1)
    status(piece2)
    status(piece3)
    status(piece4)
        
'''
Used after a piece has moved. First checks to see if the piece is on a protected tile. 
If it is not, it will check to see of any of the other pieces of a different color are on the same tile.
If another piece is on the same tile, then that other piece has its index reset and is sent to jail.
'''
def eat(piece,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    if piece.index == 1 or piece.index == 8 or piece.index == 13 or piece.index == 18 or piece.index == 25 or piece.index == 30 or piece.index == 35 or piece.index == 42 or piece.index == 47 or piece.index == 52 or piece.index == 59 or piece.index >= 64:
        pass
    else:
        otherpieces = [other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12]
        tile = piece.track[piece.index]
        for i in otherpieces:
            if i.index > 72:
                i.index == 72
            if i.track[i.index] == tile:
                i.index = 0 

#Repeats the eat method for every piece of a color
def eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    eat(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    eat(piece2,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    eat(piece3,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    eat(piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

'''Used whenever a piece that was in jail leaves jail. Any piece of a different color that was on the
 relevant piece's starting tile is sent to their respective jail. '''
def stomp(piece,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    otherpieces = [other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12]
    start = piece.track[1]
    for i in otherpieces:
        if i.track[i.index] == start:
            i.index = 0
        
#Used whenever doubles is rolled. Checks every piece of a color to see if it is in jail if it was, changes its index to that of its starting tile
def freeFromJail(piece1,piece2,piece3,piece4):
    if piece1.inJail:
        piece1.index = 1
    if piece2.inJail:
        piece2.index = 1
    if piece3.inJail:
        piece3.index = 1
    if piece4.inJail:
        piece4.index = 1

'''Used at the beginning of a move to update the status of a piece based on the index and the values of the dice rolled.
Checks if the piece is limited in its movements at all due to proximity to the finishing tile. '''
def closeSafe(piece,dice1,dice2):
    spacesLeft = 72 - piece.index
    notAllowed = 0
    if spacesLeft < dice1:
        piece.closeDice1 = True
        notAllowed += 1
    else:
        piece.closeDice1 = False
    if spacesLeft < dice2:
        piece.closeDice2 = True
        notAllowed += 1
    else:
        piece.closeDice2 = False
    if spacesLeft < (dice1 + dice2):
        piece.closeCombined = True
        notAllowed += 1
    else:
        piece.closeCombined = False
    if notAllowed < 3:
        piece.closeMove = False
    else:
        piece.closeMove = True
    if piece.index == 72:
        piece.closeMove = False

#Repeats the closeSafe method for every piece of a color
def closeSafeAll(piece1,piece2,piece3,piece4,dice1,dice2):
    closeSafe(piece1,dice1,dice2)
    closeSafe(piece2,dice1,dice2)
    closeSafe(piece3,dice1,dice2)
    closeSafe(piece4,dice1,dice2)

'''
Top level method used for decision making on the possible moves a player can make.
Updates the statuses of a piece based on updates from the previous moves.
Then, 
    -   sums up the number of pieces that are in jail in numInJail
    -   sums up the number of pieces that are done in numDone
    -   sums up the number of pieces unable to move due to their proximity to the finishing tile and the values of the dice in numTooClose
With the numbers of pieces with each status known, a large selection structure chooses from 15 algorithms, called strats
'''
def mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    

    statusAll(piece1,piece2,piece3,piece4)

    numInJail = 0
    if piece1.inJail:
        numInJail += 1
    if piece2.inJail:
        numInJail += 1
    if piece3.inJail:
        numInJail += 1
    if piece4.inJail:
        numInJail += 1

    numDone = 0
    if piece1.done:
        numDone += 1
    if piece2.done:
        numDone += 1
    if piece3.done:
        numDone += 1
    if piece4.done:
        numDone += 1
        

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)


    closeSafeAll(piece1,piece2,piece3,piece4,dice1,dice2)
    numTooClose = 0
    if piece1.closeMove:
        numTooClose += 1
    if piece2.closeMove:
        numTooClose += 1
    if piece3.closeMove:
        numTooClose += 1
    if piece4.closeMove:
        numTooClose += 1
    
    #Strat 1
    if numInJail == 4 or (numInJail == 3 and numDone == 1) or (numInJail == 2 and numDone == 2) or (numInJail == 1 and numDone == 3):
        strat1(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

    #Strat 2
    elif (numInJail == 2 and numTooClose == 1 and numDone == 0) or (numInJail == 2 and numDone == 1 and numTooClose == 0) or (numInJail == 3 and numDone == 0 and numTooClose == 0):
        strat2(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
   
    #Strat 3
    elif (numInJail == 1 and numTooClose == 2 and numDone == 0) or (numInJail == 1 and numDone == 1 and numTooClose == 1):
        strat3(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
    #Strat 4
    elif numInJail == 2 and numDone == 0 and numTooClose == 0:
        strat4(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
    #Strat 5
    elif (numInJail == 1 and numTooClose == 1 and numDone == 0) or (numInJail == 1 and numDone == 1 and numTooClose == 0):
        strat5(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
   
    #Strat 6
    elif (numInJail == 0 and numDone == 0 and numTooClose == 2) or (numInJail == 0 and numDone == 1 and numTooClose == 1) or (numInJail == 0 and numDone == 2 and numTooClose == 0):
        strat6(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
   
   #Strat 7
    elif (numInJail == 1 and numDone == 0 and numTooClose == 0):
        strat7(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
    #Strat 8
    elif (numInJail == 0 and numDone == 0 and numTooClose == 1) or (numInJail == 0 and numDone == 1 and numTooClose == 0):
        strat8(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
    #Strat 9
    elif (numInJail == 0 and numDone == 0 and numTooClose == 0):
        strat9(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
    #Strat 10
    elif numTooClose == 4 or (numDone == 1 and numTooClose == 3) or (numDone == 2 and numTooClose == 2):
        strat10(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
    #strat 11
    elif (numInJail == 1 and numTooClose == 3) or (numInJail == 2 and numTooClose == 2) or (numInJail == 3 and numTooClose == 1) or (numInJail == 1 and numDone == 1 and numTooClose == 2) or (numInJail == 1 and numDone == 2 and numTooClose == 1) or (numInJail == 2 and numDone == 1 and numTooClose == 1):
        strat11(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
    #Strat 12
    elif (numInJail == 0 and numDone == 0 and numTooClose == 3) or (numInJail == 0 and numDone == 1 and numTooClose == 2) or (numInJail == 0 and numDone == 2 and numTooClose == 1):
        strat12(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
   
   #Strat 13
    elif numInJail == 0 and numDone == 3 and numTooClose == 0:
        strat13(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
   
    #Strat 14
    elif numInJail == 1 and numDone == 2 and numTooClose == 0:
        strat14(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
   
    #Strat 15
    else:
        strat15(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
    

#Roll in mainMove is Ignored. Roll Up to Three Times for Doubles. If Doubles Rolled, Free Pieces From Jail.  
def strat1(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12):
    for i in range(3):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == dice2:
            freeFromJail(piece1,piece2,piece3,piece4)
            break
    if dice1 == dice2:
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12) 

#Used in cases when only one piece is movable. Depending on the status of the piece, different moves will be played.
def decideFor1(piece,dice1,dice2):
    if not piece.closeCombined:
        piece.index += dice1 + dice2
    
    elif not (piece.closeDice1 or piece.closeDice2):
        piece.index += max(dice1,dice2)
    
    else:
        piece.index += min(dice1,dice2)

#If Doubles are Rolled, Free the Pieces in Jail. Else, Move the One Free Piece.
def strat2(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if dice1 == dice2:
        freeFromJail(piece1,piece2,piece3,piece4)
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    
    else:
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            decideFor1(piece1,dice1,dice2)
        
        elif not (piece2.inJail or piece2.done or piece2.closeMove):
            decideFor1(piece2,dice1,dice2)
        
        elif not (piece3.inJail or piece3.done or piece3.closeMove):
            decideFor1(piece3,dice1,dice2)
        
        else:
            decideFor1(piece4,dice1,dice2)
        
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

#If Doubles are Rolled, Free the One Piece in Jail and Move the One Free Piece. Else, Move the One Free Piece.
def strat3(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if dice1 == dice2:
        freeFromJail(piece1,piece2,piece3,piece4)
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            piece1.index += dice1
        
        elif not (piece2.inJail or piece2.done or piece2.closeMove):
            piece2.index += dice1
        
        elif not (piece3.inJail or piece3.done or piece3.closeMove):
            piece3.index += dice1
        
        else:
            piece4.index += dice1
        
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    
    else:
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            decideFor1(piece1,dice1,dice2)
        
        elif not (piece2.inJail or piece2.done or piece2.closeMove):
            decideFor1(piece2,dice1,dice2)
        
        elif not (piece3.inJail or piece3.done or piece3.closeMove):
            decideFor1(piece3,dice1,dice2)
        
        else:
            decideFor1(piece4,dice1,dice2)
        
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

'''Used in cases when two pieces are movable. Depending on the statuses of the pieces, different possibilities of moves will be given. 
Then any one of the given possibilities is randomly chosen.'''
def decideFor2(piece1,piece2,dice1,dice2):
    p1Count = 3
    if piece1.closeCombined:
        p1Count -= 1
    if piece1.closeDice1:
        p1Count -= 1
    if piece1.closeDice2:
        p1Count -= 1

    p2Count = 3
    if piece2.closeCombined:
        p2Count -= 1
    if piece2.closeDice1:
        p2Count -= 1
    if piece2.closeDice2:
        p2Count -= 1

    if p1Count == 3 and p2Count == 3:
        randChoice = random.randint(1,4)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2

        elif randChoice == 2: 
            piece1.index += dice2
            piece2.index += dice1

        elif randChoice == 3:
            piece1.index += dice1 + dice2

        else:
            piece2.index += dice1 + dice2
    
    elif p1Count == 3 and p2Count == 2:
        randChoice = random.randint(1,3)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2

        elif randChoice == 2: 
            piece1.index += dice2
            piece2.index += dice1

        else:
            piece1.index += dice1 + dice2

    elif p1Count == 2 and p2Count == 3:
        randChoice = random.randint(1,3)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2

        elif randChoice == 2: 
            piece1.index += dice2
            piece2.index += dice1

        else:
            piece2.index += dice1 + dice2
    
    elif p1Count == 2 and p2Count == 2:
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2

        else:
            piece1.index += dice2
            piece2.index += dice1

    elif (p1Count == 3 and p2Count == 1):
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece1.index += max(dice1,dice2)
            piece2.index += min(dice1,dice2)

        else:
            piece1.index += dice1 + dice2

    elif (p1Count == 1 and p2Count == 3):
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece1.index += min(dice1,dice2)
            piece2.index += max(dice1,dice2)

        else:
            piece2.index += dice1 + dice2
    
    elif (p1Count == 2 and p2Count == 1):
        piece1.index += max(dice1,dice2)
        piece2.index += min(dice1,dice2)
    
    elif (p1Count == 1 and p2Count == 2):
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)
    else:
        randChoice = random.randint(1,2)
        if randChoice == 1:
            piece1.index += min(dice1,dice2)

        else:
            piece2.index += min(dice1,dice2)

#Helper method that, based on the statuses of the pieces, puts the pieces able to move into a list, which is then returned.
def constructArguments(piece1,piece2,piece3,piece4,dice1,dice2):
    list1 = [piece1,piece2,piece3,piece4]
    list2 = []
    for i in list1:
        if not (i.inJail or i.done or i.closeMove):
            list2.append(i)

    list2.append(dice1)
    list2.append(dice2)
    return list2

#If Doubles are Rolled, Free the Pieces in Jail. Else, Decide to Move From The Two Free Pieces.
def strat4(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if dice1 == dice2:
        freeFromJail(piece1,piece2,piece3,piece4)
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    
    else:
        list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
        decideFor2(*list1)   
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12) 

#If Doubles are Rolled, Free the One Piece in Jail and Randomly Move One Free Piece. Else, Decide to Move From the Two Free Pieces.
def strat5(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if dice1 == dice2:
        freeFromJail(piece1,piece2,piece3,piece4)
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        listFree = []
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            listFree.append(piece1)

        if not (piece2.inJail or piece2.done or piece2.closeMove):
            listFree.append(piece2)

        if not (piece3.inJail or piece3.done or piece3.closeMove):
            listFree.append(piece3)

        if not (piece4.inJail or piece4.done or piece4.closeMove):
            listFree.append(piece4)

        rando = random.randint(0,1)
        listFree[rando].index += dice1
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    
    else:
        list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
        decideFor2(*list1)
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

#Decide to Move From the Two Free Pieces. 
def strat6(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
    decideFor2(*list1)
    eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)   
    if dice1 == dice2:
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

#Helper method which helps construct arguments for the decideFor3 method by sorting by how free each piece is to move
def input3(piece1,piece2,piece3,p1,p2,p3):
    list1 = [[piece1,p1],[piece2,p2],[piece3,p3]]
    list1.sort(key=lambda piece: piece[1])
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i][0])
    return list2

'''The following seven methods are helper methods for the decideFor3 method.
By sorting the pieces by their freedom of movement in the input3 method, one block of code can be used
to give the possible moves for multiple different combinations of moves, greatly reducing code length'''
def zeroOneTwo(piece1,piece2,piece3,dice1,dice2):
    randChoice = random.randint(1,8)
    if randChoice == 1:
        piece1.index += dice1
        piece2.index += dice2

    elif randChoice == 2:
        piece1.index += dice1
        piece3.index += dice2

    elif randChoice == 3:
        piece2.index += dice1
        piece3.index += dice2

    elif randChoice == 4:
        piece1.index += dice2
        piece2.index += dice1

    elif randChoice == 5:
        piece1.index += dice2
        piece3.index += dice1

    elif randChoice == 6:
        piece2.index += dice2
        piece3.index += dice1

    elif randChoice == 7:
        piece2.index += dice1 + dice2

    else:
        piece3.index += dice1 + dice2

def zeroTwoOne(piece1,piece2,piece3,dice1,dice2):
    randChoice = random.randint(1,7)
    if randChoice == 1:
        piece1.index += dice1
        piece2.index += dice2

    elif randChoice == 2:
        piece1.index += dice1
        piece3.index += dice2

    elif randChoice == 3:
        piece2.index += dice1
        piece3.index += dice2

    elif randChoice == 4:
        piece1.index += dice2
        piece2.index += dice1

    elif randChoice == 5:
        piece1.index += dice2
        piece3.index += dice1

    elif randChoice == 6:
        piece2.index += dice2
        piece3.index += dice1

    else:
        piece3.index += dice1 + dice2

def oneZeroTwo(piece1,piece2,piece3,dice1,dice2):
    randChoice = random.randint(1,6)
    if randChoice == 1:
        piece3.index += dice1
        piece2.index += dice2

    elif randChoice == 2:
        piece3.index += max(dice1,dice2)
        piece1.index += min(dice1,dice2)

    elif randChoice == 3:
        piece2.index += max(dice1,dice2)
        piece1.index += min(dice1,dice2)

    elif randChoice == 4:
        piece3.index += dice2
        piece2.index += dice1

    elif randChoice == 5:
        piece3.index += dice1 + dice2

    else:
        piece2.index += dice1 + dice2

def twoZeroOne(piece1,piece2,piece3,dice1,dice2):
    randChoice = random.randint(1,3)
    if randChoice == 1:
        piece3.index += max(dice1,dice2)
        piece2.index += min(dice1,dice2)

    elif randChoice == 2:
        piece3.index += max(dice1,dice2)
        piece1.index += min(dice1,dice2)

    else:
        piece3.index += dice1 + dice2

def oneTwoZero(piece1,piece2,piece3,dice1,dice2):
    randChoice = random.randint(1,4)
    if randChoice == 1:
        piece3.index += dice1
        piece2.index += dice2

    elif randChoice == 2:
        piece3.index += max(dice1,dice2)
        piece1.index += min(dice1,dice2)

    elif randChoice == 3:
        piece2.index += max(dice1,dice2)
        piece1.index += min(dice1,dice2)

    else:
        piece3.index += dice2
        piece2.index += dice1

def twoOneZero(piece1,piece2,piece3,dice1,dice2):
    randChoice = random.randint(1,2)
    if randChoice == 1:
        piece3.index += max(dice1,dice2)
        piece1.index += min(dice1,dice2)

    else:
        piece3.index += max(dice1,dice2)
        piece2.index += min(dice1,dice2)

def oneOneOne(piece1,piece2,piece3,dice1,dice2):
    randChoice = random.randint(1,5)
    if randChoice == 1:
        piece3.index += dice1
        piece2.index += dice2

    elif randChoice == 2:
        piece3.index += max(dice1,dice2)
        piece1.index += min(dice1,dice2)

    elif randChoice == 3:
        piece2.index += max(dice1,dice2)
        piece1.index += min(dice1,dice2)

    elif randChoice == 4:
        piece3.index += dice2
        piece2.index += dice1

    else:
        piece3.index += dice1 + dice2

'''Used in cases when three pieces are movable. Depending on the statuses of the pieces, different possibilities of moves will be given. 
Then any one of the given possibilities is randomly chosen.'''
def decideFor3(piece1,piece2,piece3,dice1,dice2):
   
    p1Count = 3
    if piece1.closeCombined:
        p1Count -= 1
    if piece1.closeDice1:
        p1Count -= 1
    if piece1.closeDice2:
        p1Count -= 1

    p2Count = 3
    if piece2.closeCombined:
        p2Count -= 1
    if piece2.closeDice1:
        p2Count -= 1
    if piece2.closeDice2:
        p2Count -= 1

    p3Count = 3
    if piece3.closeCombined:
        p3Count -= 1
    if piece3.closeDice1:
        p3Count -= 1
    if piece3.closeDice2:
        p3Count -= 1

    if p1Count == 3 and p2Count == 3 and p3Count == 3:
        randChoice = random.randint(1,9)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
        elif randChoice == 6:
            piece2.index += dice2
            piece3.index += dice1
        elif randChoice == 7:
            piece1.index += dice1 + dice2
        elif randChoice == 8:
            piece2.index += dice1 + dice2
        else:
            piece3.index += dice1 + dice2

    elif (p1Count == 2 and p2Count == 3 and p3Count == 3) or (p1Count == 3 and p2Count == 2 and p3Count == 3) or (p1Count == 3 and p2Count == 3 and p3Count == 2):
        list1 = input3(piece1,piece2,piece3,p1Count,p2Count,p3Count)
        list1.append(dice1)
        list1.append(dice2)
        zeroOneTwo(*list1)

    elif (p1Count == 2 and p2Count == 2 and p3Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 2) or (p1Count == 3 and p2Count == 2 and p3Count == 2):
        list1 = input3(piece1,piece2,piece3,p1Count,p2Count,p3Count)
        list1.append(dice1)
        list1.append(dice2)
        zeroTwoOne(*list1)
        
    elif p1Count == 2 and p2Count == 2 and p3Count == 2:
        randChoice = random.randint(1,6)
        if randChoice == 1:
            piece1.index += dice1
            piece2.index += dice2
        elif randChoice == 2:
            piece1.index += dice1
            piece3.index += dice2
        elif randChoice == 3:
            piece2.index += dice1
            piece3.index += dice2
        elif randChoice == 4:
            piece1.index += dice2
            piece2.index += dice1
        elif randChoice == 5:
            piece1.index += dice2
            piece3.index += dice1
        else:
            piece2.index += dice2
            piece3.index += dice1

    elif (p1Count == 3 and p2Count == 3 and p3Count == 1) or (p1Count == 3 and p2Count == 1 and p3Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 3):
        list1 = input3(piece1,piece2,piece3,p1Count,p2Count,p3Count)
        list1.append(dice1)
        list1.append(dice2)
        oneZeroTwo(*list1)
    
    elif (p1Count == 3 and p2Count == 1 and p3Count == 1) or (p1Count == 1 and p2Count == 3 and p3Count == 1) or (p1Count == 1 and p2Count == 1 and p3Count == 3):
        list1 = input3(piece1,piece2,piece3,p1Count,p2Count,p3Count)
        list1.append(dice1)
        list1.append(dice2)
        twoZeroOne(*list1)

    elif p1Count == 1 and p2Count == 1 and p3Count == 1:
        randChoice = random.randint(1,3)
        if randChoice == 1:
            piece1.index += min(dice1,dice2)
        elif randChoice == 2:
            piece2.index += min(dice1,dice2)
        else:
            piece3.index += min(dice1,dice2)

    elif (p1Count == 2 and p2Count == 2 and p3Count == 1) or (p1Count == 2 and p2Count == 1 and p3Count == 2) or (p1Count == 1 and p2Count == 2 and p3Count == 2):
        list1 = input3(piece1,piece2,piece3,p1Count,p2Count,p3Count)
        list1.append(dice1)
        list1.append(dice2)
        oneTwoZero(*list1)

    elif (p1Count == 2 and p2Count == 1 and p3Count == 1) or (p1Count == 1 and p2Count == 2 and p3Count == 1) or (p1Count == 1 and p2Count == 1 and p3Count == 2):
        list1 = input3(piece1,piece2,piece3,p1Count,p2Count,p3Count)
        list1.append(dice1)
        list1.append(dice2)
        twoOneZero(*list1)

    else:
        list1 = input3(piece1,piece2,piece3,p1Count,p2Count,p3Count)
        list1.append(dice1)
        list1.append(dice2)
        oneOneOne(*list1)

#If Doubles Are Rolled, Free the One Piece From Free and Move One Free Piece. Else, Decide to Move From the Three Free Pieces. 
def strat7(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if dice1 == dice2:
        freeFromJail(piece1,piece2,piece3,piece4)
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        listFree = []
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            listFree.append(piece1)

        if not (piece2.inJail or piece2.done or piece2.closeMove):
            listFree.append(piece2)

        if not (piece3.inJail or piece3.done or piece3.closeMove):
            listFree.append(piece3)

        if not (piece4.inJail or piece4.done or piece4.closeMove):
            listFree.append(piece4)

        rando = random.randint(0,2)
        listFree[rando].index += dice1
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    
    else:
        list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
        decideFor3(*list1)
        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)   

#Decide to Move From the Three Free Pieces.
def strat8(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    list1 = constructArguments(piece1,piece2,piece3,piece4,dice1,dice2)
    decideFor3(*list1)
    eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)  
    if dice1 == dice2:
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

#Helper method which helps construct arguments for the decideFor4 method by sorting by how free each piece is to move
def input4(piece1,piece2,piece3,piece4,p1,p2,p3,p4):
    list1 = [[piece1,p1],[piece2,p2],[piece3,p3],[piece4,p4]]
    list1.sort(key=lambda piece: piece[1])
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i][0])
    return list2

'''The following twelve methods are helper methods for the decideFor4 method.
By sorting the pieces by their freedom of movement in the input4 method, one block of code can be used
to give the possible moves for multiple different combinations of moves, greatly reducing code length'''
def zeroOneThree(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,15)
    if rando == 1:
        piece1.index += dice1
        piece2.index += dice2

    elif rando == 2:
        piece1.index += dice1
        piece3.index += dice2

    elif rando == 3:
        piece1.index += dice1
        piece4.index += dice2

    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2

    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2

    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2

    elif rando == 7:
        piece1.index += dice2
        piece2.index += dice1

    elif rando == 8:
        piece1.index += dice2
        piece3.index += dice1

    elif rando == 9:
        piece1.index += dice2
        piece4.index += dice1

    elif rando == 10:
        piece2.index += dice2
        piece3.index += dice1

    elif rando == 11:
        piece2.index += dice2
        piece4.index += dice1

    elif rando == 12:
        piece3.index += dice2
        piece4.index += dice1

    elif rando == 13:
        piece2.index += dice1 + dice2

    elif rando == 14:
        piece3.index += dice1 + dice2

    else:
        piece4.index += dice1 + dice2      
    
def zeroTwoTwo(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,14)
    if rando == 1:
        piece1.index += dice1
        piece2.index += dice2

    elif rando == 2:
        piece1.index += dice1
        piece3.index += dice2

    elif rando == 3:
        piece1.index += dice1
        piece4.index += dice2

    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2

    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2

    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2

    elif rando == 7:
        piece1.index += dice2
        piece2.index += dice1

    elif rando == 8:
        piece1.index += dice2
        piece3.index += dice1

    elif rando == 9:
        piece1.index += dice2
        piece4.index += dice1

    elif rando == 10:
        piece2.index += dice2
        piece3.index += dice1

    elif rando == 11:
        piece2.index += dice2
        piece4.index += dice1

    elif rando == 12:
        piece3.index += dice2
        piece4.index += dice1

    elif rando == 13:
        piece3.index += dice1 + dice2

    else:
        piece4.index += dice1 + dice2  

def zeroThreeOne(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,13)
    if rando == 1:
        piece1.index += dice1
        piece2.index += dice2

    elif rando == 2:
        piece1.index += dice1
        piece3.index += dice2

    elif rando == 3:
        piece1.index += dice1
        piece4.index += dice2

    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2

    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2

    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2

    elif rando == 7:
        piece1.index += dice2
        piece2.index += dice1

    elif rando == 8:
        piece1.index += dice2
        piece3.index += dice1

    elif rando == 9:
        piece1.index += dice2
        piece4.index += dice1

    elif rando == 10:
        piece2.index += dice2
        piece3.index += dice1

    elif rando == 11:
        piece2.index += dice2
        piece4.index += dice1

    elif rando == 12:
        piece3.index += dice2
        piece4.index += dice1

    else:
        piece4.index += dice1 + dice2

def oneZeroThree(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,12)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)

    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 3:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2

    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2

    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2

    elif rando == 7:
        piece2.index += dice2
        piece3.index += dice1

    elif rando == 8:
        piece2.index += dice2
        piece4.index += dice1

    elif rando == 9:
        piece3.index += dice2
        piece4.index += dice1

    elif rando == 10:
        piece2.index += dice1 + dice2

    elif rando == 11:
        piece3.index += dice1 + dice2

    else:
        piece4.index += dice1 + dice2

def oneOneTwo(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,11)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)

    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 3:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2

    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2

    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2

    elif rando == 7:
        piece2.index += dice2
        piece3.index += dice1

    elif rando == 8:
        piece2.index += dice2
        piece4.index += dice1

    elif rando == 9:
        piece3.index += dice2
        piece4.index += dice1

    elif rando == 10:
        piece3.index += dice1 + dice2

    else:
        piece4.index += dice1 + dice2

def oneTwoOne(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,10)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)

    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 3:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2

    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2

    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2

    elif rando == 7:
        piece2.index += dice2
        piece3.index += dice1

    elif rando == 8:
        piece2.index += dice2
        piece4.index += dice1

    elif rando == 9:
        piece3.index += dice2
        piece4.index += dice1

    else:
        piece4.index += dice1 + dice2

def oneThreeZero(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,9)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece2.index += max(dice1,dice2)

    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 3:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 4:
        piece2.index += dice1
        piece3.index += dice2

    elif rando == 5:
        piece2.index += dice1
        piece4.index += dice2

    elif rando == 6:
        piece3.index += dice1
        piece4.index += dice2

    elif rando == 7:
        piece2.index += dice2
        piece3.index += dice1

    elif rando == 8:
        piece2.index += dice2
        piece4.index += dice1

    else:
        piece3.index += dice2
        piece4.index += dice1

def twoZeroTwo(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,8)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 3:
        piece2.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 4:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 5:
        piece3.index += dice1
        piece4.index += dice2

    elif rando == 6:
        piece3.index += dice2
        piece4.index += dice1

    elif rando == 7:
        piece3.index += dice1 + dice2

    else:
        piece4.index += dice1 + dice2
    
def twoOneOne(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,7)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 3:
        piece2.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 4:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 5:
        piece3.index += dice1
        piece4.index += dice2

    elif rando == 6:
        piece3.index += dice2
        piece4.index += dice1

    else:
        piece4.index += dice1 + dice2

def twoTwoZero(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,6)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 2:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 3:
        piece2.index += min(dice1,dice2)
        piece3.index += max(dice1,dice2)

    elif rando == 4:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 5:
        piece3.index += dice1
        piece4.index += dice2

    else:
        piece3.index += dice2
        piece4.index += dice1

def threeZeroOne(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,4)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 2:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 3:
        piece3.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    else:
        piece4.index += dice1 + dice2
    
def threeOneZero(piece1,piece2,piece3,piece4,dice1,dice2):
    rando = random.randint(1,3)
    if rando == 1:
        piece1.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    elif rando == 2:
        piece2.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

    else:
        piece3.index += min(dice1,dice2)
        piece4.index += max(dice1,dice2)

'''Used in cases when four pieces are movable. Depending on the statuses of the pieces, different possibilities of moves will be given. 
Then any one of the given possibilities is randomly chosen.'''
def decideFor4(piece1,piece2,piece3,piece4,dice1,dice2):
    
    p1Count = 3
    if piece1.closeCombined:
        p1Count -= 1
    if piece1.closeDice1:
        p1Count -= 1
    if piece1.closeDice2:
        p1Count -= 1

    p2Count = 3
    if piece2.closeCombined:
        p2Count -= 1
    if piece2.closeDice1:
        p2Count -= 1
    if piece2.closeDice2:
        p2Count -= 1

    p3Count = 3
    if piece3.closeCombined:
        p3Count -= 1
    if piece3.closeDice1:
        p3Count -= 1
    if piece3.closeDice2:
        p3Count -= 1

    p4Count = 3
    if piece4.closeCombined:
        p4Count -= 1
    if piece4.closeDice1:
        p4Count -= 1
    if piece4.closeDice2:
        p4Count -= 1

    if (p1Count == 3 and p2Count == 3 and p3Count == 3 and p4Count == 3):
        rando = random.randint(1,16)
        if rando == 1:
            piece1.index += dice1
            piece2.index += dice2

        elif rando == 2:
            piece1.index += dice1
            piece3.index += dice2

        elif rando == 3:
            piece1.index += dice1
            piece4.index += dice2

        elif rando == 4:
            piece2.index += dice1
            piece3.index += dice2

        elif rando == 5:
            piece2.index += dice1
            piece4.index += dice2

        elif rando == 6:
            piece3.index += dice1
            piece4.index += dice2

        elif rando == 7:
            piece1.index += dice2
            piece2.index += dice1

        elif rando == 8:
            piece1.index += dice2
            piece3.index += dice1

        elif rando == 9:
            piece1.index += dice2
            piece4.index += dice1

        elif rando == 10:
            piece2.index += dice2
            piece3.index += dice1

        elif rando == 11:
            piece2.index += dice2
            piece4.index += dice1

        elif rando == 12:
            piece3.index += dice2
            piece4.index += dice1

        elif rando == 13:
            piece1.index += dice1 + dice2

        elif rando == 14:
            piece2.index += dice1 + dice2

        elif rando == 15:
            piece3.index += dice1 + dice2

        else:
            piece4.index += dice1 + dice2

    elif (p1Count == 2 and p2Count == 3 and p3Count == 3 and p4Count == 3) or (p1Count == 3 and p2Count == 2 and p3Count == 3 and p4Count == 3) or (p1Count == 3 and p2Count == 3 and p3Count == 2 and p4Count == 3) or (p1Count == 3 and p2Count == 3 and p3Count == 3 and p4Count == 2):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        zeroOneThree(*list2)

    elif (p1Count == 2 and p2Count == 2 and p3Count == 3 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 2 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 3 and p4Count == 2) or (p1Count == 3 and p2Count == 2 and p3Count == 2 and p4Count == 3) or (p1Count == 3 and p2Count == 2 and p3Count == 3 and p4Count == 2) or (p1Count == 3 and p2Count == 3 and p3Count == 2 and p4Count == 2):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        zeroTwoTwo(*list2)

    elif (p1Count == 2 and p2Count == 2 and p3Count == 2 and p4Count == 3) or (p1Count == 2 and p2Count == 2 and p3Count == 3 and p4Count == 2) or (p1Count == 2 and p2Count == 3 and p3Count == 2 and p4Count == 2) or (p1Count == 3 and p2Count == 2 and p3Count == 2 and p4Count == 2):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        zeroThreeOne(*list2)

    elif p1Count == 2 and p2Count == 2 and p3Count == 2 and p4Count == 2:
        rando = random.randint(1,12)
        if rando == 1:
            piece1.index += dice1
            piece2.index += dice2

        elif rando == 2:
            piece1.index += dice1
            piece3.index += dice2

        elif rando == 3:
            piece1.index += dice1
            piece4.index += dice2

        elif rando == 4:
            piece2.index += dice1
            piece3.index += dice2

        elif rando == 5:
            piece2.index += dice1
            piece4.index += dice2

        elif rando == 6:
            piece3.index += dice1
            piece4.index += dice2

        elif rando == 7:
            piece1.index += dice2
            piece2.index += dice1

        elif rando == 8:
            piece1.index += dice2
            piece3.index += dice1

        elif rando == 9:
            piece1.index += dice2
            piece4.index += dice1

        elif rando == 10:
            piece2.index += dice2
            piece3.index += dice1

        elif rando == 11:
            piece2.index += dice2
            piece4.index += dice1

        else:
            piece3.index += dice2
            piece4.index += dice1

    elif (p1Count == 1 and p2Count == 3 and p3Count == 3 and p4Count == 3) or (p1Count == 3 and p2Count == 1 and p3Count == 3 and p4Count == 3) or (p1Count == 3 and p2Count == 3 and p3Count == 1 and p4Count == 3) or (p1Count == 3 and p2Count == 3 and p3Count == 3 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        oneZeroThree(*list2)

    elif (p1Count == 1 and p2Count == 2 and p3Count == 3 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 2 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 3 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 3 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 1 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 1 and p3Count == 2 and p4Count == 3) or (p1Count == 3 and p2Count == 1 and p3Count == 3 and p4Count == 2) or (p1Count == 3 and p2Count == 2 and p3Count == 1 and p4Count == 3) or (p1Count == 3 and p2Count == 2 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 3 and p3Count == 1 and p4Count == 2) or (p1Count == 3 and p2Count == 3 and p3Count == 2 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        oneOneTwo(*list2)

    elif (p1Count == 1 and p2Count == 2 and p3Count == 2 and p4Count == 3) or (p1Count == 1 and p2Count == 2 and p3Count == 3 and p4Count == 2) or (p1Count == 1 and p2Count == 3 and p3Count == 2 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 2 and p4Count == 3) or (p1Count == 2 and p2Count == 1 and p3Count == 3 and p4Count == 2) or (p1Count == 3 and p2Count == 1 and p3Count == 2 and p4Count == 2) or (p1Count == 2 and p2Count == 2 and p3Count == 1 and p4Count == 3) or (p1Count == 2 and p2Count == 3 and p3Count == 1 and p4Count == 2) or (p1Count == 3 and p2Count == 2 and p3Count == 1 and p4Count == 2) or (p1Count == 2 and p2Count == 2 and p3Count == 3 and p4Count == 1) or (p1Count == 2 and p2Count == 3 and p3Count == 2 and p4Count == 1) or (p1Count == 3 and p2Count == 2 and p3Count == 2 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        oneTwoOne(*list2)

    elif (p1Count == 1 and p2Count == 2 and p3Count == 2 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 2 and p4Count == 2) or (p1Count == 2 and p2Count == 2 and p3Count == 1 and p4Count == 2) or (p1Count == 2 and p2Count == 2 and p3Count == 2 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        oneThreeZero(*list2)

    elif (p1Count == 1 and p2Count == 1 and p3Count == 3 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 1 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 1 and p3Count == 1 and p4Count == 3) or (p1Count == 3 and p2Count == 1 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 3 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        twoZeroTwo(*list2)
     
    elif (p1Count == 1 and p2Count == 1 and p3Count == 2 and p4Count == 3) or (p1Count == 1 and p2Count == 1 and p3Count == 3 and p4Count == 2) or (p1Count == 1 and p2Count == 2 and p3Count == 1 and p4Count == 3) or (p1Count == 1 and p2Count == 3 and p3Count == 1 and p4Count == 2) or (p1Count == 1 and p2Count == 2 and p3Count == 3 and p4Count == 1) or (p1Count == 1 and p2Count == 3 and p3Count == 2 and p4Count == 1) or (p1Count == 2 and p2Count == 1 and p3Count == 1 and p4Count == 3) or (p1Count == 3 and p2Count == 1 and p3Count == 1 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 3 and p4Count == 1) or (p1Count == 3 and p2Count == 1 and p3Count == 2 and p4Count == 1) or (p1Count == 2 and p2Count == 3 and p3Count == 1 and p4Count == 1) or (p1Count == 3 and p2Count == 2 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        twoOneOne(*list2)

    elif (p1Count == 1 and p2Count == 1 and p3Count == 2 and p4Count == 2) or (p1Count == 1 and p2Count == 2 and p3Count == 1 and p4Count == 2) or (p1Count == 1 and p2Count == 2 and p3Count == 2 and p4Count == 1) or (p1Count == 2 and p2Count == 1 and p3Count == 1 and p4Count == 2) or (p1Count == 2 and p2Count == 1 and p3Count == 2 and p4Count == 1) or (p1Count == 2 and p2Count == 2 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        twoTwoZero(*list2)
    
    elif (p1Count == 1 and p2Count == 1 and p3Count == 1 and p4Count == 3) or (p1Count == 1 and p2Count == 1 and p3Count == 3 and p4Count == 1) or (p1Count == 1 and p2Count == 3 and p3Count == 1 and p4Count == 1) or (p1Count == 3 and p2Count == 1 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        threeZeroOne(*list2)

    elif (p1Count == 1 and p2Count == 1 and p3Count == 1 and p4Count == 2) or (p1Count == 1 and p2Count == 1 and p3Count == 2 and p4Count == 1) or (p1Count == 1 and p2Count == 2 and p3Count == 1 and p4Count == 1) or (p1Count == 2 and p2Count == 1 and p3Count == 1 and p4Count == 1):
        list2 = input4(piece1,piece2,piece3,piece4,p1Count,p2Count,p3Count,p4Count)
        list2.append(dice1)
        list2.append(dice2)
        threeOneZero(*list2)

    else:
        rando = random.randint(1,4)
        if rando == 1:
            piece1.index += min(dice1,dice2)
        elif rando == 2:
            piece2.index += min(dice1,dice2)
        elif rando == 3:
            piece3.index += min(dice1,dice2)
        else:
            piece4.index += min(dice1,dice2)

#Decide to Move From the Four Free Pieces.
def strat9(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    decideFor4(piece1,piece2,piece3,piece4,dice1,dice2)
    eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)    
    if dice1 == dice2:
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

#If No Doubles Are Rolled, The Turn is Skipped.
def strat10(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if dice1 == dice2:
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

#If Doubles Are Rolled, Free the Piece(s) From Jail. Else, the Turn is Skipped.
def strat11(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if dice1 == dice2:
        freeFromJail(piece1,piece2,piece3,piece4)
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        
'''Move the One Free Piece With the Values From Both Dice. 
If the Sum of the Values of the Dice is Greater than the Number of Spaces the Piece is Away From the Finishing Tile, 
Then the Piece Moves with the Greater Value, and the Lesser Value is Thrown Out. Doubles Still Apply.'''
def strat12(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if not (piece1.inJail or piece1.done or piece1.closeMove):
        decideFor1(piece1,dice1,dice2)

    elif not (piece2.inJail or piece2.done or piece2.closeMove):
        decideFor1(piece2,dice1,dice2)

    elif not (piece3.inJail or piece3.done or piece3.closeMove):
        decideFor1(piece3,dice1,dice2)

    else:
        decideFor1(piece4,dice1,dice2)

    eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
    if dice1 == dice2:
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)

#Like strat12, Except When the Free Piece is Within Six Spaces of the Finishing Tile, Only One Die is Rolled.
def strat13(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if not (piece1.inJail or piece1.done or piece1.closeMove):
        onePiece = piece1

    elif not (piece2.inJail or piece2.done or piece2.closeMove):
        onePiece = piece2

    elif not (piece3.inJail or piece3.done or piece3.closeMove):
        onePiece = piece3

    else:
        onePiece = piece4

    dist = 72 - onePiece.index
    if dist > 6:
        strat12(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
    else:
        rando = random.randint(1,6)
        if rando <= dist:
            onePiece.index += rando

#Like strat12, Except When Doubles Are Rolled, Free the One Piece in Jail and Move the One Free Piece
def strat14(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if dice1 == dice2:
        freeFromJail(piece1,piece2,piece3,piece4)
        stomp(piece1,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        if not (piece1.inJail or piece1.done or piece1.closeMove):
            piece1.index += dice1

        elif not (piece2.inJail or piece2.done or piece2.closeMove):
            piece2.index += dice1

        elif not (piece3.inJail or piece3.done or piece3.closeMove):
            piece3.index += dice1

        else:
            piece4.index += dice1

        eatAll(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12)
        mainMove(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12) 
    else:
        strat12(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2)
    
#One Die. If the Value is Greater Than the Number of Spaces Between the Piece and the Finishing Tile, Then Skip the Turn.
def strat15(piece1,piece2,piece3,piece4,other1,other2,other3,other4,other5,other6,other7,other8,other9,other10,other11,other12,dice1,dice2):
    if not piece1.done:
        onePiece = piece1

    elif not piece2.done:
        onePiece = piece2

    elif not piece3.done:
        onePiece = piece3

    else:
        onePiece = piece4

    dist = 72 - onePiece.index
    rando = random.randint(1,6)
    if rando <= dist:
        onePiece.index += rando


#simulates the game a certain number of times, then prints the amount of times each color won and the percentage of times they won
def simulate(num):
    redWins = 0
    blueWins = 0
    greenWins = 0
    yellowWins = 0
    for i in range(num):
        red1 = redPiece()
        red2 = redPiece()
        red3 = redPiece()
        red4 = redPiece()

        green1 = greenPiece()
        green2 = greenPiece()
        green3 = greenPiece()
        green4 = greenPiece()

        blue1 = bluePiece()
        blue2 = bluePiece()
        blue3 = bluePiece()
        blue4 = bluePiece()

        yellow1 = yellowPiece()
        yellow2 = yellowPiece()
        yellow3 = yellowPiece()
        yellow4 = yellowPiece()
        rando = random.randint(1,4)
        if rando == 1:
            while (red1.index < 72 or red2.index < 72 or red3.index < 72 or red4.index < 72) and (green1.index < 72 or green2.index < 72 or green3.index < 72 or green4.index < 72) and (blue1.index < 72 or blue2.index < 72 or blue3.index < 72 or blue4.index < 72) and (yellow1.index < 72 or yellow2.index < 72 or yellow3.index < 72 or yellow4.index < 72):
                mainMove(red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4)
                if red1.index == 72 and red2.index == 72 and red3.index == 72 and red4.index == 72:
                    redWins += 1
                    break

                mainMove(green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4)
                if green1.index == 72 and green2.index == 72 and green3.index == 72 and green4.index == 72:
                    greenWins += 1
                    break

                mainMove(blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4)
                if blue1.index == 72 and blue2.index == 72 and blue3.index == 72 and blue4.index == 72:
                    blueWins += 1
                    break

                mainMove(yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4) 
                if yellow1.index == 72 and yellow2.index == 72 and yellow3.index == 72 and yellow4.index == 72:
                    yellowWins += 1
                    break

        elif rando == 2:
            while (red1.index < 72 or red2.index < 72 or red3.index < 72 or red4.index < 72) and (green1.index < 72 or green2.index < 72 or green3.index < 72 or green4.index < 72) and (blue1.index < 72 or blue2.index < 72 or blue3.index < 72 or blue4.index < 72) and (yellow1.index < 72 or yellow2.index < 72 or yellow3.index < 72 or yellow4.index < 72):
                mainMove(green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4)
                if green1.index == 72 and green2.index == 72 and green3.index == 72 and green4.index == 72:
                    greenWins += 1
                    break

                mainMove(blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4)
                if blue1.index == 72 and blue2.index == 72 and blue3.index == 72 and blue4.index == 72:
                    blueWins += 1
                    break

                mainMove(yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4)
                if yellow1.index == 72 and yellow2.index == 72 and yellow3.index == 72 and yellow4.index == 72:
                    yellowWins += 1
                    break

                mainMove(red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4)  
                if red1.index == 72 and red2.index == 72 and red3.index == 72 and red4.index == 72:
                    redWins += 1
                    break

        elif rando == 3:
            while (red1.index < 72 or red2.index < 72 or red3.index < 72 or red4.index < 72) and (green1.index < 72 or green2.index < 72 or green3.index < 72 or green4.index < 72) and (blue1.index < 72 or blue2.index < 72 or blue3.index < 72 or blue4.index < 72) and (yellow1.index < 72 or yellow2.index < 72 or yellow3.index < 72 or yellow4.index < 72):
                mainMove(blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4)
                if blue1.index == 72 and blue2.index == 72 and blue3.index == 72 and blue4.index == 72:
                    blueWins += 1
                    break

                mainMove(yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4)
                if yellow1.index == 72 and yellow2.index == 72 and yellow3.index == 72 and yellow4.index == 72:
                    yellowWins += 1
                    break

                mainMove(red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4)
                if red1.index == 72 and red2.index == 72 and red3.index == 72 and red4.index == 72:
                    redWins += 1
                    break

                mainMove(green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4) 
                if green1.index == 72 and green2.index == 72 and green3.index == 72 and green4.index == 72:
                    greenWins += 1
                    break 

        elif rando == 4:
            while (red1.index < 72 or red2.index < 72 or red3.index < 72 or red4.index < 72) and (green1.index < 72 or green2.index < 72 or green3.index < 72 or green4.index < 72) and (blue1.index < 72 or blue2.index < 72 or blue3.index < 72 or blue4.index < 72) and (yellow1.index < 72 or yellow2.index < 72 or yellow3.index < 72 or yellow4.index < 72):
                mainMove(yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4)
                if yellow1.index == 72 and yellow2.index == 72 and yellow3.index == 72 and yellow4.index == 72:
                    yellowWins += 1
                    break

                mainMove(red1,red2,red3,red4,green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4)
                if red1.index == 72 and red2.index == 72 and red3.index == 72 and red4.index == 72:
                    redWins += 1
                    break

                mainMove(green1,green2,green3,green4,blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4)
                if green1.index == 72 and green2.index == 72 and green3.index == 72 and green4.index == 72:
                    greenWins += 1
                    break

                mainMove(blue1,blue2,blue3,blue4,yellow1,yellow2,yellow3,yellow4,red1,red2,red3,red4,green1,green2,green3,green4)
                if blue1.index == 72 and blue2.index == 72 and blue3.index == 72 and blue4.index == 72:
                    blueWins += 1
                    break

        if (i+1) % 50 == 0:
            print(i+1)
            
    print("red wins: " + str(redWins) + " | green wins: " + str(greenWins) + " | blue wins: " + str(blueWins) + " | yellow wins: " + str(yellowWins))
    print("(Percentages) red: " + str(redWins/num) + " | green: " + str(greenWins/num) + " | blue: " + str(blueWins/num) + " | yellow: " + str(yellowWins/num))

numSims = int(input("How many times do you want to simulate Parques? "))
simulate(numSims)
