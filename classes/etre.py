import math 

class etre :
    def __init__(self,name):
        self.name= name

class Monster(etre):
    def __init__(self,name,type,hp,attack,defense):
        super().__init__(name)
        self.type=type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.weapon=[]

# reste a definir plus tard

class personnage(etre) :
    def __init__(self,name):
        super().__init__(name)
        self.hp = 100
        self.level = 1
        self.xp= 500
        self.attack = 25
        self.defense = 25
        self.inventaire = []
        self.weapon=[]

    def verif_level(self):
        temp = self.level 
        niveau = math.floor(math.sqrt(self.xp/500))
        if niveau == temp :
            print("Vous n'avez pas changez de niveau")
        else:
            self.level = niveau
            print(f"Vous êtes passé au niveau {self.level}")
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


