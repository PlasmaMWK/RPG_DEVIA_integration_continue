class Personnage:
    def __init__(self):
        self.hp = 10

    def recevoir_degats(self):
        self.hp -= 1