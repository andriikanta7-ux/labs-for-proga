def find_unreachable_cities(cities, storages, pipelines):
    graph = {}
    
    for a, b in pipelines:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    
    result = []

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

    for storage in storages:
        reachable = dfs(storage)

        unreachable_cities = []
        for city in cities:
            if city not in reachable:
                unreachable_cities.append(city)

        if unreachable_cities:
            result.append([storage, unreachable_cities])  

    return result
