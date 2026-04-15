def num_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
    ]

    def dfs(r, c):
        stack = [(r, c)]
        visited[r][c] = True

        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows and
                    0 <= ny < cols and
                    not visited[nx][ny] and
                    grid[nx][ny] == 1
                ):
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count