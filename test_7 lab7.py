import unittest
import copy
from lab_7level3 import edmonds_karp, defaultdict


class TestMaxFlow(unittest.TestCase):

    def setUp(self):
        self.graph = defaultdict(lambda: defaultdict(int))

        self.source = 'SRC'
        self.sink = 'SNK'

        self.graph['SRC']['F1'] = 10
        self.graph['SRC']['F2'] = 5

        self.graph['F1']['X1'] = 10
        self.graph['F2']['X1'] = 5

        self.graph['X1']['S1'] = 7
        self.graph['X1']['S2'] = 8

        self.graph['S1']['SNK'] = 7
        self.graph['S2']['SNK'] = 8

    def test_max_flow(self):
        result = edmonds_karp(copy.deepcopy(self.graph), self.source, self.sink)
        self.assertEqual(result, 15)

    def test_zero_flow(self):
        graph = defaultdict(lambda: defaultdict(int))
        graph['SRC']['F1'] = 0
        graph['F1']['SNK'] = 0

        result = edmonds_karp(graph, 'SRC', 'SNK')
        self.assertEqual(result, 0)

    def test_single_path(self):
        graph = defaultdict(lambda: defaultdict(int))
        graph['SRC']['A'] = 5
        graph['A']['SNK'] = 5

        result = edmonds_karp(graph, 'SRC', 'SNK')
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()