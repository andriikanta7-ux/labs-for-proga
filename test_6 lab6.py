import unittest

def find_unreachable_cities(cities, storages, pipelines):
    graph = {}

    for a, b in pipelines:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)

    def dfs(start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in graph.get(node, []):
                    stack.append(neighbor)

        return visited

    result = []

    for storage in storages:
        reachable = dfs(storage)
        unreachable = [city for city in cities if city not in reachable]

        if unreachable:
            result.append([storage, unreachable])

    return result


class TestGasNetwork(unittest.TestCase):

    def test_all_reachable(self):
        cities = ['A', 'B']
        storages = ['S1']
        pipelines = [['S1', 'A'], ['A', 'B']]

        self.assertEqual(find_unreachable_cities(cities, storages, pipelines), [])

    def test_one_unreachable(self):
        cities = ['A', 'B', 'C']
        storages = ['S1']
        pipelines = [['S1', 'A'], ['A', 'B']]

        self.assertEqual(
            find_unreachable_cities(cities, storages, pipelines),
            [['S1', ['C']]]
        )

    def test_multiple_storages(self):
        cities = ['A', 'B']
        storages = ['S1', 'S2']
        pipelines = [['S1', 'A']]

        self.assertEqual(
            find_unreachable_cities(cities, storages, pipelines),
            [
                ['S1', ['B']],
                ['S2', ['A', 'B']]
            ]
        )

    def test_no_pipelines(self):
        cities = ['A', 'B']
        storages = ['S1']
        pipelines = []

        self.assertEqual(
            find_unreachable_cities(cities, storages, pipelines),
            [['S1', ['A', 'B']]]
        )

    def test_cycle(self):
        cities = ['A', 'B']
        storages = ['S1']
        pipelines = [['S1', 'A'], ['A', 'B'], ['B', 'A']]

        self.assertEqual(
            find_unreachable_cities(cities, storages, pipelines),
            []
        )


if __name__ == "__main__":
    unittest.main()