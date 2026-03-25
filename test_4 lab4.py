import unittest
from lab_4level3 import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_inorder(self):
        self.pq.insert("A", 5)
        self.pq.insert("B", 2)
        self.pq.insert("C", 8)
        self.pq.insert("D", 1)

        result = self.pq.inorder()
        expected = [("D", 1), ("B", 2), ("A", 5), ("C", 8)]
        self.assertEqual(result, expected)

    def test_peek(self):
        self.pq.insert("A", 5)
        self.pq.insert("B", 2)
        self.pq.insert("D", 1)

        self.assertEqual(self.pq.peek(), ("D", 1))

    def test_delete_min(self):
        self.pq.insert("A", 5)
        self.pq.insert("B", 2)
        self.pq.insert("D", 1)

        removed = self.pq.delete_min()
        self.assertEqual(removed, "D")

        self.assertEqual(self.pq.peek(), ("B", 2))

    def test_delete_until_empty(self):
        self.pq.insert("A", 3)
        self.pq.insert("B", 1)

        self.assertEqual(self.pq.delete_min(), "B")
        self.assertEqual(self.pq.delete_min(), "A")
        self.assertIsNone(self.pq.delete_min())

    def test_empty_peek(self):
        self.assertIsNone(self.pq.peek())

    def test_single_element(self):
        self.pq.insert("X", 10)

        self.assertEqual(self.pq.peek(), ("X", 10))
        self.assertEqual(self.pq.delete_min(), "X")
        self.assertIsNone(self.pq.peek())


if __name__ == "__main__":
    unittest.main()