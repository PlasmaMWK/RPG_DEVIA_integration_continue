from main import Personnage

import unittest

class Tests(unittest.TestCase):
    def test_hp_equals_10(self):
        personnage = Personnage()
        self.assertEqual(personnage.hp, 10)

    def test_attaquant_enleve_1hp(self):
        self.assertEqual(personnage.hp, 9)

if __name__ == "__main__":
    unittest.main()