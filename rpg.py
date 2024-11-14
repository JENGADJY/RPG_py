from classes.etre import personnage, Monster, type_interactions
from classes.objet import Potion
from classes.weapon import weapon
import random
from map import Map
from classes.etre import monstres


#probleme d'import 
knife=weapon("Knife","physical",50)
magic_book=weapon("magic_book","magic",75)
sword = weapon("Sword", "Physical", 70)   
axe = weapon("Axe", "Physical", 90)       
staff = weapon("Staff", "Magic", 60)     
crossbow = weapon("Crossbow", "Physical", 80)  
dagger = weapon("Dagger", "Physical", 40)  
fire_staff = weapon("Fire Staff", "Magic", 100)  
lightning_wand = weapon("Lightning Wand", "Magic", 90)  
holy_sword = weapon("Holy Sword", "Physical", 85)  
armes = [knife, sword, axe, magic_book, staff, crossbow, dagger, fire_staff, lightning_wand, holy_sword]

physical_weapons = [
    weapon("Knife", "Physical", 50),
    weapon("Sword", "Physical", 70),
    weapon("Axe", "Physical", 90),
    weapon("Crossbow", "Physical", 80),
    weapon("Dagger", "Physical", 40),
    weapon("Holy Sword", "Physical", 85),
]


magic_weapons = [
    weapon("Magic Book", "Magic", 75),
    weapon("Staff", "Magic", 60),
    weapon("Fire Staff", "Magic", 100),
    weapon("Lightning Wand", "Magic", 90),
]

skeleton_weapons = [
    weapon("Bone Dagger", "Physical", 45),
    weapon("Skeleton Shield", "Physical", 35),
]


ntr = weapon("N**** Ta race","dragon",500),
hellfire = weapon("HELL'S FIRE","dragon",1000),
ahbah = weapon("AH BAH","dragon",10000)


        

healing_potion = Potion("Potion de soin", "heal", 30)  # Restaure 30 HP
attack_buff_potion = Potion("Potion de force", "attack", 10)  # Augmente l'attaque de 10
defense_buff_potion = Potion("Potion de défense", "defense", 10)  # Augmente la défense de 10
mana_potion = Potion("Potion de mana", "heal", 20)  # Restaure 20 HP (si tu as un système de mana)
speed_buff_potion = Potion("Potion de rapidité", "attack", 5)  # Augmente la vitesse d'attaque (hypothétique)
strength_potion = Potion("Potion de force supérieure", "attack", 20)  # Augmente l'attaque de 20
invincibility_potion = Potion("Potion d'invincibilité", "defense", 50)  # Augmente la défense de 50 pour un tour
poison_potion = Potion("Potion de poison", "attack", -15)  # Inflige 15 dégâts à l'ennemi lors de l'utilisation
revival_potion = Potion("Potion de résurrection", "heal", 100)  # Restaure 100 HP
critical_hit_potion = Potion("Potion de coup critique", "attack", 15)  # Augmente les chances de coup critique

potions = [
    healing_potion,
    attack_buff_potion,
    defense_buff_potion,
    mana_potion,
    speed_buff_potion,
    strength_potion,
    invincibility_potion,
    poison_potion,
    revival_potion,
    critical_hit_potion
]


def RPG():
    c = input("Please enter your name: ")
    character = personnage(c)
    
    print("What weapon do you like:")
    print("1. Knife")
    print("2. Magic book")
    first_weapon = int(input())

    if first_weapon == 1:
        print("Vous avez obtenu un couteau")
        character.weapon.append(knife) 
    elif first_weapon == 2:
        print("Vous avez obtenu un livre magique")
        character.weapon.append(magic_book) 
    else:
        print("Choix invalide. Sortie du jeu.")
        exit()

    if len(character.weapon) == 0:
        print("Vous n'avez pas d'arme équipée. Vous ne pouvez pas attaquer.")
        return  

    print(f"Character's weapon: {[weapon.name for weapon in character.weapon]}")
    game_map = Map(10, 10)
    game_map.personnage = character
    boss = Monster("Dark Lord", 500, 50, 1000, 1000)
    boss.weapon.append(ntr,hellfire,ahbah)

    game_map.ajouter_boss(boss, 4, 4)  
    
    
    game_map.declencher_combat()  
    while True:
        direction = input("Entrez une direction pour déplacer le joueur (up, down, left, right) : ")
        if direction == 'save':
            from save import saving
            saving(character,game_map)  
        else:
            game_map.deplacer_personnage(direction)
            game_map.declencher_evenement_aleatoire()




def combat(personnage, ennemi):
    print(f"Vous combattez {ennemi.name}!")

    while personnage.hp > 0 and ennemi.hp > 0:
        print(f"\nQue voulez-vous faire ?")
        print("1. Attaquer")
        print("2. Utiliser un objet")
        print("3. Fuir")
        
        action = int(input("Choix (entier seulement accepté) : "))

        if action == 1:
            
            damage(personnage, ennemi)
            if ennemi.hp <= 0:  
                print(f"{ennemi.name} a été vaincu!")
                reward_character(personnage,ennemi)
                break
            
            ennemie_attack(ennemi, personnage)
            if personnage.hp <= 0:  
                print(f"{personnage.name} a été vaincu!")
                print("Vous avez perdu")
                exit()
                
        elif action == 2:
            
            personnage.use_object()
            if personnage.hp <= 0:  
                print(f"{personnage.name} n'a pas survécu à l'attaque de l'ennemi après avoir utilisé un objet.")
                break
        elif action == 3:
            print(f"{personnage.name} a fui le combat.")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 3.")
            
        print(f"\nÉtat actuel : {personnage.name} - HP: {personnage.hp}, {ennemi.name} - HP: {ennemi.hp}")


def damage(personnage, ennemi):
    if len(personnage.weapon) > 0:
        
        weapon = personnage.use_weapon()
        damage_dealt = weapon.attack()  
        print(f"{personnage.name} attaque avec {weapon.name} et inflige {damage_dealt} dégâts à {ennemi.name}.")
        ennemi.hp -= damage_dealt
    else:
        print(f"{personnage.name} n'a pas d'arme équipée et ne peut pas attaquer.")


def ennemie_attack(ennemi, personnage):
    if len(ennemi.weapon) > 0:
        weapon = ennemi.use_weapon()
        damage_dealt = weapon.attack()
        print(f"{ennemi.name} attaque avec {weapon.name} et inflige {damage_dealt} dégâts à {personnage.name}.")
        personnage.hp -= damage_dealt
    else:
        damage_dealt = random.randint(5, 10) 
        print(f"{ennemi.name} attaque avec ses griffes et inflige {damage_dealt} dégâts à {personnage.name}.")
        personnage.hp -= damage_dealt



def reward_character(character, ennemi):
    xp_gained = ennemi.hp + ennemi.attack  
    character.xp += xp_gained
    print(f"{character.name} a gagné {xp_gained} points d'expérience!")

    character.verif_level()

    weapon = get_weapon_for_enemy(ennemi.type)
    if weapon:
        if len(character.weapon) >= 4:  
            print("Vous avez déjà 4 armes. Choisissez une arme à remplacer :")
            for i, w in enumerate(character.weapon):
                print(f"{i}: {w.name}")
            
            choice = int(input(f"Choisissez l'index de l'arme à remplacer contre {weapon} : "))
            if 0 <= choice < len(character.weapon):
                replaced_weapon = character.weapon[choice]
                character.weapon[choice] = weapon
                print(f"{character.name} a remplacé {replaced_weapon.name} par {weapon.name}!")
            else:
                print("Choix invalide. Aucune arme n'a été remplacée.")
        else:
            character.weapon.append(weapon)
            print(f"{character.name} a obtenu une nouvelle arme: {weapon.name}!")

    potion = random.choice(potions)  
    character.inventaire.append(potion)  
    print(f"{character.name} a obtenu une nouvelle potion: {potion.name}!")

        
def get_weapon_for_enemy(enemy_type):
    if enemy_type == "Physique":
        return random.choice(physical_weapons)
    elif enemy_type == "Magique":
        return random.choice(magic_weapons)
    elif enemy_type == "Squelette":
        return random.choice(skeleton_weapons)
    return None
