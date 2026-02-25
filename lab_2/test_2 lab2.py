import unittest
from lab_2level2 import min_eating_speed

class TestBananaEating(unittest.TestCase):
    
    def test_example_1(self):
        piles = [3, 6, 7, 11]
        H = 8
        self.assertEqual(min_eating_speed(piles, H), 4)
    
    def test_example_2(self):
        piles = [30, 11, 23, 4, 20]
        H = 5
        self.assertEqual(min_eating_speed(piles, H), 30)
    
    def test_example_3(self):
        piles = [30, 11, 23, 4, 20]
        H = 6
        self.assertEqual(min_eating_speed(piles, H), 23)

if __name__ == "__main__":
    unittest.main()
