from rpg import RPG
from classes.weapon import weapon
from rpg import armes, potions
import json
from map import Map
from save import saving


def load():
    try:
        with open('save_game.json', 'r') as save_file:
            game_data = json.load(save_file)
            from classes.etre import personnage
            character_data = game_data['character']
            character = personnage(character_data['name'])
            character.hp = character_data['hp']
            character.level = character_data['level']
            character.xp = character_data['xp']
            
            for weapon_name in character_data['weapon']:
                for weapon in armes:
                    if weapon.name == weapon_name:
                        character.weapon.append(weapon)

            for potion_name in character_data['inventaire']:
                for potion in potions:
                    if potion.name == potion_name:
                        character.inventaire.append(potion)
            
            game_map = Map(game_data['map']['largeur'], game_data['map']['hauteur'])
            game_map.player_position = character_data['position']  
            game_map.personnage = character 

            print(f"Jeu chargé. Bienvenue de retour, {character.name}!")
            return character, game_map

    except FileNotFoundError:
        print("Aucun fichier de sauvegarde trouvé.")
        return None, None

def continue_game(character, game_map):
    print(f"Reprise du jeu avec {character.name} à la position {game_map.player_position[0]}, {game_map.player_position[1]}.")

    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Se déplacer")
        print("2. Vérifier l'inventaire")
        print("3. Vérifier les stats du personnage")
        print("4. Sauvegarder et quitter")
        print("5. Quitter sans sauvegarder")
        
        choice = int(input("Choix (entier seulement accepté) : "))
        
        if choice == 1:
            direction = input("Entrez une direction pour déplacer le joueur (up, down, left, right) : ")
            game_map.deplacer_personnage(direction)
            game_map.declencher_evenement_aleatoire()
        elif choice == 2:
            print(f"{character.name} - Inventaire: {[item.name for item in character.inventaire]}")
        elif choice == 3:
            print(f"{character.name} - HP: {character.hp}, Level: {character.level}, XP: {character.xp}")
        elif choice == 4:
            saving(character, game_map)
            print("Jeu sauvegardé et quitté.")
            break
        elif choice == 5:
            print(f"{character.name} quitte le jeu sans sauvegarder.")
            break
        else:
            print("Choix invalide. Essayez encore.")


    

def main():
    print("MAIN MENU:")
    print("1. Create New Game")
    print("2. Continue Game")
    print("3. About")
    print("4. Exit")
    
    c = int(input("Choix : "))

    if c == 1:
        RPG()  
    elif c == 2:
        character, game_map = load()
        if character and game_map:
            continue_game(character, game_map)
    elif c == 3:
        print("C'est un rpg ,y'a pas de lore ou jsp quoi ")
    elif c == 4:
        print("Sortie du jeu.")
        exit()
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()
