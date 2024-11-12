from rpg import RPG

def main():
    print("MAIN MENU:")
    print("1. Create New Game")
    print("2. About")
    print("3. Exit")
    c = int(input())

    if c == 1:
        RPG()
    elif c == 2:
        print("À propos du jeu...")
    elif c == 3:
        print("Sortie du jeu.")
        exit()
    else:
        print("Choix invalide.")

main()