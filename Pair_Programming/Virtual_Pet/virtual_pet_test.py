import unittest
from Pikachu import *

class virtual_pet_test(unittest.TestCase):
    def setUp(self):
        print('Start before the test')

    def tearDown(self):
        print('Print after the test')


    def test_get_hungriness(self):
        pet = Tamagotchi('Pikachu')
        self.assertEqual(pet.get_hungriness, 50)

    def test_get_fullness(self):
        pet = Tamagotchi('Pikachu')
        self.assertEqual(pet.get_fullness, 50)

    def test_feed(self):
        pet = Tamagotchi('Pikachu')
        self.assertEqual(pet.Feed_Tamagotchi(), (40, 60))

    def test_play(self):
        pet = Tamagotchi('Pikachu')
        self.assertEqual(pet.Play_Tamagotchi(), (10, 10))

    def test_sleep(self):
        pet = Tamagotchi('Pikachu')
        self.assertEqual(pet.Sleep_Tamagotchi(), 0)

    def test_poop(self):
        pet = Tamagotchi('Pikachu')
        self.assertEqual(pet.Poop_Tamagotchi(), 40)

if __name__ == '__main__':
    unittest().main()
