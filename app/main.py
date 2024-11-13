class Personnage:
    def __init__(self):
        self.hp = 10

    def recevoir_degats(self):
        self.hp -= 1

    def est_mort(self):
        if self.hp <= 0:
            return True
        return False
    
    def est_vivant(self):
        if self.hp > 0:
            return True
        return False
    
    def est_blesse(self):
        if self.hp < 10 and self.hp > 0:
            return True
<<<<<<< HEAD
        return False
    
    #Coucou c'est un test 4
=======
        return False
>>>>>>> 3e5da20 ([GREEN] test est blesse OK)
