from etre import personnage

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