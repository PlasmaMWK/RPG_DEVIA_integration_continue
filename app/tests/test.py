import unittest

class Tests(unittest.TestCase):
    def test_hp_equals_10(self):
        personnage = Personnage()
        self.assertEqual(personnage.hp, 10)

    

 