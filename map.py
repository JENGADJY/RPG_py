import random
class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = [[" " for _ in range(cols)] for _ in range(rows)]
        self.player_position = [0, 0]  

    def afficher_map(self):
        for r in range(self.rows):
            row = ""
            for c in range(self.cols):
                if [r, c] == self.player_position:
                    row += "P "  
                else:
                    row += self.map[r][c] + " " 
            print(row)

    def ajouter_boss(self, boss, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            self.boss = boss
            self.map[x][y] = boss  
            print(f"Le boss {boss.name} a été ajouté à la position ({x}, {y}) sur la carte.")
        else:
            print("Pas ajouté.")


    def deplacer_personnage(self, direction):
        x, y = self.player_position
        if direction == 'up' and x > 0:
            self.player_position = [x - 1, y]
        elif direction == 'down' and x < self.rows - 1:
            self.player_position = [x + 1, y]
        elif direction == 'left' and y > 0:
            self.player_position = [x, y - 1]
        elif direction == 'right' and y < self.cols - 1:
            self.player_position = [x, y + 1]
        elif direction == 'Exit':
            exit()
        else:
            print("rien a ete fait")


        
        self.afficher_map()

    def declencher_evenement_aleatoire(self):
        evenement = random.choice(["combat", "rien"])
        if evenement == "combat":
            print("Un combat se déclenche !")
            self.declencher_combat()
        else:
            print("Rien ne se passe ici.")
    
    def declencher_combat(self):
        from rpg import combat,monstres
        from classes.etre import personnage
        monstre = random.choice(monstres) 
        print(f"Un {monstre.name} apparaît !")
        combat(self.personnage, monstre)
