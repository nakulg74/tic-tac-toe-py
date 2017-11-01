#Nakul Gupta
#2017068
#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

import random
from random import randint as randi
# There are 2 players: player1 and player2
player1=1
player2=2


# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2

tile1= 0    
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0

# turn variable defines whose turn is now
turn = player1

def validmove(move):
    """ Checks whether a move played by a player is valid or invalid.
        Return True if move is valid. 
        
        A move is valid if the corresponding tile for the move is not ticked.
    """
    if move == 1:
        if tile1 != 0:
            return False
        else:
            return True
    if move == 2:
        if tile2 != 0:
            return False
        else:
            return True
    if move == 3:
        if tile3 != 0:
            return False
        else:
            return True
    if move == 4:
        if tile4 != 0:
            return False
        else:
            return True
    if move == 5:
        if tile5 != 0:
            return False
        else:
            return True
    if move == 6:
        if tile6 != 0:
            return False
        else:
            return True
    if move == 7:
        if tile7 != 0:
            return False
        else:
            return True
    if move == 8:
        if tile8 != 0:
            return False
        else:
            return True
    if move == 9:
        if tile9 != 0:
            return False
        else:
            return True

def win():
    """ Returns True if the board state specifies a winning state for some player.
        
        A player wins if ticks made by the player are present either
        i) in a row
        ii) in a cloumn
        iii) in a diagonal
    """
    if tile1==tile2==tile3!=0:
        return True
    elif tile4==tile5==tile6!=0:
        return True
    elif tile7==tile8==tile9!=0:
        return True
    elif tile1==tile4==tile7!=0:
        return True
    elif tile2==tile5==tile8!=0:
        return True
    elif tile3==tile6==tile9!=0:
        return True
    elif tile1==tile5==tile9!=0:
        return True
    elif tile3==tile5==tile7!=0:
        return True
    else:
        return False
    
def takeNaiveMove():
    """ Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
    """
    choice=randi(1,9)
    x=validmove(choice)
    if x:
        return choice
    else:
        takeNaiveMove()

def takeStrategicMove():
    """ Returns a tile number from the set of unchecked tiles
    using some rules.
    
    """
    #if player 1 is intelligent
    if turn==1:
        if tile1==tile2==1 and validmove(3):
            return 3
        elif tile1==tile3==1 and validmove(2):
            return 2
        elif tile2==tile3==1 and validmove(1):
            return 1
        
        elif tile4==tile5==1 and validmove(6):
            return 6
        elif tile4==tile6==1 and validmove(5):
            return 5
        elif tile5==tile6==1 and validmove(4):
            return 4
        
        elif tile7==tile8==1 and validmove(9):
            return 9
        elif tile7==tile9==1 and validmove(8):
            return 8
        elif tile8==tile9==1 and validmove(7):
            return 7
        
        elif tile1==tile4==1 and validmove(7):
            return 7
        elif tile1==tile7==1 and validmove(4):
            return 4
        elif tile4==tile7==1 and validmove(1):
            return 1
        
        elif tile2==tile5==1 and validmove(8):
            return 8
        elif tile2==tile8==1 and validmove(5):
            return 5
        elif tile5==tile8==1 and validmove(2):
            return 2
        
        elif tile3==tile6==1 and validmove(9):
            return 9
        elif tile3==tile9==1 and validmove(6):
            return 6
        elif tile6==tile9==1 and validmove(3):
            return 3
        
        elif tile1==tile5==1 and validmove(9):
            return 9
        elif tile1==tile9==1 and validmove(5):
            return 5
        elif tile5==tile9==1 and validmove(1):
            return 1
        
        elif tile3==tile5==1 and validmove(7):
            return 7
        elif tile3==tile7==1 and validmove(5):
            return 5
        elif tile5==tile7==1 and validmove(3):
            return 3
        
    #if player 2 is intelligent
    if turn==2:
        if tile1==tile2==1 and validmove(3):
            return 3
        elif tile1==tile3==1 and validmove(2):
            return 2
        elif tile2==tile3==1 and validmove(1):
            return 1
        
        elif tile4==tile5==1 and validmove(6):
            return 6
        elif tile4==tile6==1 and validmove(5):
            return 5
        elif tile5==tile6==1 and validmove(4):
            return 4
        
        elif tile7==tile8==1 and validmove(9):
            return 9
        elif tile7==tile9==1 and validmove(8):
            return 8
        elif tile8==tile9==1 and validmove(7):
            return 7
        
        elif tile1==tile4==1 and validmove(7):
            return 7
        elif tile1==tile7==1 and validmove(4):
            return 4
        elif tile4==tile7==1 and validmove(1):
            return 1
        
        elif tile2==tile5==1 and validmove(8):
            return 8
        elif tile2==tile8==1 and validmove(5):
            return 5
        elif tile5==tile8==1 and validmove(2):
            return 2
        
        elif tile3==tile6==1 and validmove(9):
            return 9
        elif tile3==tile9==1 and validmove(6):
            return 6
        elif tile6==tile9==1 and validmove(3):
            return 3
        
        elif tile1==tile5==1 and validmove(9):
            return 9
        elif tile1==tile9==1 and validmove(5):
            return 5
        elif tile5==tile9==1 and validmove(1):
            return 1
        
        elif tile3==tile5==1 and validmove(7):
            return 7
        elif tile3==tile7==1 and validmove(5):
            return 5
        elif tile5==tile7==1 and validmove(3):
            return 3

def validBoard():
    """ Return True if board state is valid.
        
        A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
    """
    count1 = 0
    count2 = 0
    if tile1==1:
        count1 = count1+1
    elif tile1==2:
        count2 = count2+1
    
    if tile2==1:
        count1 = count1+1
    elif tile2==2:
        count2 = count2+1
    
    if tile3==1:
        count1 = count1+1
    elif tile3==2:
        count2 = count2+1
    
    if tile4==1:
        count1 = count1+1
    elif tile4==2:
        count2 = count2+1
    
    if tile5==1:
        count1 = count1+1
    elif tile5==2:
        count2 = count2+1
    
    if tile6==1:
        count1 = count1+1
    elif tile6==2:
        count2 = count2+1
    
    if tile7==1:
        count1 = count1+1
    elif tile7==2:
        count2 = count2+1
    
    if tile8==1:
        count1 = count1+1
    elif tile8==2:
        count2 = count2+1
    
    if tile9==1:
        count1 = count1+1
    elif tile9==2:
        count2 = count2+1
    
    
    if count1==count2 or count1-1==count2:
        return True
    else:
        return False

def change(a,b):
    global tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile7, tile8, tile9
    
    if a==1:
        if b==1:
            tile1==b
        elif b==2:
            tile1==b
    elif a==2:
        if b==1:
            tile2==b
        elif b==2:
            tile2==b
    elif a==3:
        if b==1:
            tile3==b
        elif b==2:
            tile3==b
    elif a==4:
        if b==1:
            tile4==b
        elif b==2:
            tile4==b
    elif a==5:
        if b==1:
            tile5==b
        elif b==2:
            tile5==b
    elif a==6:
        if b==1:
            tile6==b
        elif b==2:
            tile6==b
    elif a==7:
        if b==1:
            tile7==b
        elif b==2:
            tile7==b
    elif a==8:
        if b==1:
            tile8==b
        elif b==2:
            tile8==b
    elif a==9:
        if b==1:
            tile9==b
        elif b==2:
            tile9==b

def game(gametype=1):
    """ Returns 1 if player1 wins and 2 if player2 wins
        and 0 if it is a draw.
    
        gametype defines three types of games discussed above.
        i.e., game1, game2, game3
    """
    global turn
    
    if gametype==1:
        if turn==1:
            tile1=0
            tile2=0
            tile3=0
            tile4=0
            tile5=0
            tile6=0
            tile7=0
            tile8=0
            tile9=0
            while validBoard():
                s=takeNaiveMove()
                change(s,turn)
                if win():
                    if turn==1:
                        return 1
                    else:
                        return 2
                elif not win() and tile1==tile2==tile3==tile4==tile5==tile6==tile7==tile8==tile9:
                    return 0
                if turn==1:
                    turn=2
                else:
                    turn=1
    if gametype==2:
        if turn==1:
            tile1=0
            tile2=0
            tile3=0
            tile4=0
            tile5=0
            tile6=0
            tile7=0
            tile8=0
            tile9=0
            while validBoard():
                s=takeStrategicMove()
                change(s,turn)
                if win():
                    if turn==1:
                        return 1
                    else:
                        return 2
                elif not win() and tile1==tile2==tile3==tile4==tile5==tile6==tile7==tile8==tile9:
                    return 0
                if turn==1:
                    turn=2
                else:
                    turn=1
    if gametype==3:
        if turn==1:
            tile1=0
            tile2=0
            tile3=0
            tile4=0
            tile5=0
            tile6=0
            tile7=0
            tile8=0
            tile9=0
            while validBoard():
                s=takeStrategicMove()
                change(s,turn)
                if win():
                    if turn==1:
                        return 1
                    else:
                        return 2
                elif not win() and tile1==tile2==tile3==tile4==tile5==tile6==tile7==tile8==tile9:
                    return 0
                if turn==1:
                    turn=2
                else:
                    turn=1

def game1(n):
    """ Returns the winning probability for player1. 
    
    n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
    """
    count=0
    for i in range(n):
        x=game(1)
        if x==1:
            count=count+1
    probab=float(count)/float(n)
    return probab

def game2(n):
    """Returns the winning probability for player1.
    
    n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
    """
    count=0
    for i in range(n):
        x=game(2)
        if x==1:
            count=count+1
    probab=float(count)/float(n)
    return probab

def game3(n):
    """Returns the winning probability for player1. 
    
    n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
    """
    count=0
    for i in range(n):
        x=game(3)
        if x==1:
            count=count+1
    probab=float(count)/float(n)
    return probab
