from random import randrange
import itertools
from itertools import combinations 

values = [1,2,3,4,'X',6,7,8,9]
plyr = []
comp = [5]


def displayboard(values):
    #Display the playboard with the up to date values
    print("\t+-------+-------+-------+")
    print("\t|       |       |       |")
    print("\t|   {}   |   {}   |   {}   |".format(values[0], values[1], values[2]))
    print("\t|       |       |       |")
    print('\t+-------+-------+-------+')
    print("\t|       |       |       |")
    print("\t|   {}   |   {}   |   {}   |".format(values[3], values[4], values[5]))
    print("\t|       |       |       |")
    print('\t+-------+-------+-------+')
    print("\t|       |       |       |")
    print("\t|   {}   |   {}   |   {}   |".format(values[6], values[7], values[8]))
    print("\t|       |       |       |")
    print('\t+-------+-------+-------+') 

def entermove(values):
    #Ask to user wich case he want to play in
    #check if entry is valid and modify values list
    #return True if player win
    print('Dans quel case souhaitez vous jouer ? ')
    move = int(input())
    if move <= 9 and move >= 1 :
        free = listfields(values)
        av = move in free 
        if av == True :
            plyr.append(values[move - 1])
            values[move - 1] = '0'
        else : 
            print('***************************************************\nChoix invalide, cette case est déjat prise\n***************************************************')
    else : 
            print('***************************************************\nChoix invalide, entrez une case entre 1-9\n***************************************************')
    if checkwin(plyr) == True : 
        displayboard(values)
        print('***************************************************\nHuman player win the game\n***************************************************')
        quit()
        
def listfields(values):
    #Fonction used by drawmove fonction to list all free case in wich computer choose randomly to play
    freefeilds = []
    for i in values :
        count = 0
        if i != '0' and i != 'X' :
            freefeilds.append(i)
    return freefeilds

def drawmove(values):
    #Draw the move of the computer to the board
    free = listfields(values)
    if int(randrange(len(free))) >= 0 :
        move = int(randrange(len(free)))
        freem = free[move]
        i = values.index(freem)
        comp.append(values[i])
        values[i] = 'X'
        if checkwin(comp) == True : 
            displayboard(values)
            print('***************************************************\nComputer win the game\n***************************************************')
            quit()

def rSubset(val, r): 
    #return a list of all combinations 
	return list(combinations(val, r)) 

def checkwin(val):
    #Fonction to chek if the move made to the board is a winning one
    soln = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    allposrep = []
    allposmove = []
    num_list = []
    r = 3
    for i in rSubset(val, r):
        allposrep.append(i)
    for n in allposrep :
        if len(num_list) <= 2 :
            num1 = n[0]
            num2 = n[1]
            num3 = n[2]
            num_list.append(num1)
            num_list.append(num2)
            num_list.append(num3)
            for i in range(0, 3):
                for j in range(0, 3):
                    for k in range(0, 3):
                        if(i != j & j != k & k != i):
                            val = num_list[i], num_list[j], num_list[k]
                            win = val in soln
                            if win == True : return True
            num_list = []

if __name__ == "__main__":
    while len(listfields(values)) > 0 :
        displayboard(values)
        entermove(values)
        drawmove(values)
    else :
        displayboard(values)
        print('***************************************************\nDraw Game\n***************************************************')
        quit()
