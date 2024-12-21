import unittest
from main import Personnage

class Tests(unittest.TestCase):
    def test_hp_equals_10(self):
        personnage = Personnage()
        self.assertEqual(personnage.hp(), 10)

    def test_attaquant_enleve_1hp(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_degats(attaquant)
        self.assertEqual(defenseur.hp(), 9)

    def test_attaquant_enleve_2hp(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_degats(attaquant)
        defenseur.recevoir_degats(attaquant)
        self.assertEqual(defenseur.hp(), 8)
    
    def test_0_hp_est_mort(self):
        personnage = Personnage()
        for _ in range(10):
            personnage.recevoir_degats(Personnage())
        self.assertTrue(personnage.est_mort())

    def test_1_hp_est_pas_mort(self):
        personnage = Personnage()
        for _ in range(9):
            personnage.recevoir_degats(Personnage())
        self.assertFalse(personnage.est_mort())

   
   
    def test_hp_never_negative(self):
        personnage = Personnage()
        for _ in range(15):
            personnage.recevoir_degats(Personnage())
        self.assertGreaterEqual(personnage.hp(), 0)

    def test_hp_never_exceeds_max(self):
        personnage = Personnage()
        for _ in range(15):
            personnage.recevoir_soins(1)
        self.assertLessEqual(personnage.hp(), 10)

    def test_character_can_attack(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_degats(attaquant)
        self.assertLess(defenseur.hp(), 10)

    def test_initial_hp(self):
        personnage = Personnage()
        self.assertEqual(personnage.hp(), 10)

    def test_death_status_after_damage(self):
        personnage = Personnage()
        for _ in range(10):
            personnage.recevoir_degats(Personnage())
        self.assertTrue(personnage.est_mort())




    def test_hp_after_healing(self):
        personnage = Personnage()
        personnage.recevoir_degats(Personnage())
        personnage.recevoir_soins(1)
        self.assertEqual(personnage.hp(), 10)

    def test_hp_after_multiple_healings(self):
        personnage = Personnage()
        personnage.recevoir_degats(Personnage())
        personnage.recevoir_degats(Personnage())
        personnage.recevoir_soins(1)
        personnage.recevoir_soins(1)
        self.assertEqual(personnage.hp(), 10)

    def test_hp_after_overhealing(self):
        personnage = Personnage()
        personnage.recevoir_soins(5)
        self.assertEqual(personnage.hp(), 10)

    def test_hp_after_multiple_attacks(self):
        personnage = Personnage()
        for _ in range(5):
            personnage.recevoir_degats(Personnage())
        self.assertEqual(personnage.hp(), 5)

    def test_hp_after_healing_and_damage(self):
        personnage = Personnage()
        personnage.recevoir_degats(Personnage())
        personnage.recevoir_soins(1)
        personnage.recevoir_degats(Personnage())
        self.assertEqual(personnage.hp(), 9)



if __name__ == "__main__":
    unittest.main()