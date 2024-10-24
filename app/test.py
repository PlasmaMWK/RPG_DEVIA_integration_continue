from main import Personnage

import unittest

class Tests(unittest.TestCase):
    def test_hp_equals_10(self):
        personnage = Personnage()
        self.assertEqual(personnage.hp, 10)

    def test_attaquant_enleve_1hp(self):
        personnage = Personnage()
        personnage.recevoir_degats()
        self.assertEqual(personnage.hp, 9)
    
    def test_personnage_est_mort(self):
        personnage = Personnage()
        for _ in range(10):
            personnage.recevoir_degats()
        self.assertEqual(personnage.hp, 0)
        self.assertTrue(personnage.est_mort())

    

if __name__ == "__main__":
    unittest.main()