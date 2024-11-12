

class objet:
    def __init__(self,name,effect,pda):
        self.name=name
        self.effect=effect
        self.pda=pda

    def use(self,personnage,effect):
        if effect == "attack":
            personnage.attack += self.pda
            print(f"{personnage.name} a gagné {self.pda} d'attaque.")
            return personnage.attack
        if effect == "defense":
            personnage.defense += self.pda
            print(f"{personnage.name} a gagné {self.pda} de defense.")
            return personnage.hp
        if effect == "heal":
            personnage.hp += self.pda
            print(f"{personnage.name} a gagné {self.pda} de vie.")
            return personnage.hp
        

class Potion(objet):
    def __init__(self, name, effect, pda):
        super().__init__(name, effect, pda)  






