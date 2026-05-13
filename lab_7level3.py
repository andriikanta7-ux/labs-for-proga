from collections import deque, defaultdict


def edmonds_karp(graph, source, sink):
    flow = 0
    parent = {}

    def bfs():
        visited = set()
        queue = deque([source])
        visited.add(source)
        parent.clear()

        while queue:
            u = queue.popleft()

            for v in graph[u]:
                if v not in visited and graph[u][v] > 0:
                    visited.add(v)
                    parent[v] = u

                    if v == sink:
                        return True

                    queue.append(v)

        return False

    while bfs():
        path_flow = float('inf')
        v = sink

        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        flow += path_flow

    return flow