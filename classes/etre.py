import math 

class etre :
    def __init__(self,name):
        self.name= name

class personnage(etre):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 100
        self.level = 1
        self.xp = 500
        self.attack = 25
        self.defense = 25
        self.inventaire = []
        self.weapon = []
        self.position = [0, 0]

    def verif_level(self):
        print(f"XP actuelle de {self.name}: {self.xp}")
        temp = self.level
        niveau = math.floor(math.sqrt(self.xp / 500))
    
        if niveau == temp:
            print("Vous n'avez pas changé de niveau.")
        else:
            self.level = niveau
            print(f"Vous êtes passé au niveau {self.level}")
        
        print(f"XP de {self.name} après vérification de niveau: {self.xp}")
        return self.level

    
    def use_object(self):
        print("Voici votre inventaire :")
        for i, item in enumerate(self.inventaire):
            print(f"{i}: {item.name}")  
        choice = int(input("Choisissez (entier seulement accepté) : "))
        if 0 <= choice < len(self.inventaire):
            potion = self.inventaire[choice]
            potion.use(self, potion.effect)  
            self.inventaire.pop(choice)  
        else:
            print("Choix invalide.")

    def use_weapon(self):
        print("Voici vos armes :")
        for i, item in enumerate(self.weapon):
            print(f"{i}: {item.name}") 
        print("Choisissez (entier seulement accepté) :")
        choice = int(input())
        if 0 <= choice < len(self.weapon):
            return self.weapon[choice]  
        else:
            print("Choix invalide.")
            return None
        
    def equip_weapon(self, weapon):
        self.weapon.append(weapon)





class Monster(etre):
    def __init__(self,name,type,hp,attack,defense):
        super().__init__(name)
        self.type=type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.weapon=[]

gobelin = Monster("Gobelin", "Physique", hp=30, attack=15, defense=5)
ogre = Monster("Ogre", "Physique", hp=100, attack=25, defense=15)
spectre = Monster("Spectre", "Magique", hp=40, attack=20, defense=3)
liche = Monster("Liche", "Magique", hp=80, attack=30, defense=10)
chevalier_squelette = Monster("Chevalier Squelette", "Squelette", hp=50, attack=18, defense=8)

monstres = [gobelin, ogre, spectre, liche, chevalier_squelette]

type_interactions = {
    "Physical": {
        "Gobelin": 1.0,
        "Ogre": 0.5,      
        "Spectre": 0.8,   
        "Liche": 0.5,     
        "Chevalier Squelette": 1.0,
    },
    "Magic": {
        "Gobelin": 1.5,   
        "Ogre": 1.0,      
        "Spectre": 1.0,   
        "Liche": 2.0,     
        "Chevalier Squelette": 0.5,
    }
}


