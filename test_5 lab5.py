import unittest
from lab_5level3 import num_islands


class TestNumIslands(unittest.TestCase):

    def test_example(self):
        grid = [
        [1,0,1,1,1,0,0,0,0,0],
        [1,1,1,0,1,0,1,1,1,1],
        [0,0,0,0,1,1,0,1,1,1],
        [0,1,1,0,1,0,1,1,1,1],
        [0,0,0,0,1,1,1,0,0,0],
        [1,0,1,0,1,1,0,0,0,0],
        [1,1,1,1,1,0,0,0,1,1],
        [1,1,1,0,1,1,0,0,0,1],
        [0,1,0,1,0,1,1,0,1,1],
        [0,0,0,0,1,1,1,0,0,0]
    ]
        self.assertEqual(num_islands(grid), 4) 

    def test_empty(self):
        self.assertEqual(num_islands([]), 0)

    def test_no_land(self):
        self.assertEqual(num_islands([[0,0],[0,0]]), 0)

    def test_all_land(self):
        self.assertEqual(num_islands([[1,1],[1,1]]), 1)

    def test_separate(self):
        self.assertEqual(num_islands([[1,0,1],[0,0,0],[1,0,1]]), 4)


if __name__ == "__main__":
    unittest.main()