import json
def saving(character, game_map):
    game_data = {
        'character': {
            'name': character.name,
            'hp': character.hp,
            'level': character.level,
            'xp': character.xp,
            'weapon': [weapon.name for weapon in character.weapon],
            'inventaire': [potion.name for potion in character.inventaire],
            'position': game_map.player_position,  
        },
        'map': {
            'largeur': game_map.rows,  
            'hauteur': game_map.cols,  
        }
    }

    with open('save_game.json', 'w') as save_file:
        json.dump(game_data, save_file, indent=4)
        print("Jeu sauvegardé avec succès!")
