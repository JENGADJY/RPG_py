from classes.etre import personnage
#from classes.etre import Monster
#from classes.objet import objet
from classes.weapon import weapon
from rpg import RPG



def main():
    
    print("MAIN MENU:")
    print("1.Create New Game")
    print("2.About")
    print("3.Exit")
    c= int(input())

    if c== 1:
        print("c'est bon")
        RPG()
    if c==2:
        print("tkt")
    if c==3:
        print("bref")
        exit()
    
    


main()
