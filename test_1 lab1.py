import unittest
from lab_1level1 import sorted_squares

class TestSortedSquares(unittest.TestCase):
    
    def test_example_1(self):
        nums = [-4, -2, 0, 1, 3]
        self.assertEqual(sorted_squares(nums), [0, 1, 4, 9, 16])
    
    def test_example_2(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(sorted_squares(nums), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()