# Leetcode Q. No- 1254 Number of Closed Islands

# Using Recursive DFS

from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        Count = 0
        def dfs(row, col):
            nonlocal m, n, directions
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] != 0:
                return
            grid[row][col] = 1
            for x, y in directions:
                dfs(row + x, col + y)
        for i in range(n):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][m - 1] == 0:
                dfs(i, m - 1)
        for j in range(m):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[n - 1][j] == 0:
                dfs(n - 1, j)
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    Count += 1
        return Count
    

# Using BFS

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        Count = 0
        def bfs(row, col):
            from collections import deque
            queue = deque()
            queue.append((row, col))
            grid[row][col] = 1
            while queue:
                a, b = queue.popleft()
                for x, y in directions:
                    nx, ny = a + x, b + y
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        queue.append((nx, ny))
        for i in range(n):
            if grid[i][0] == 0:
                bfs(i, 0)
            if grid[i][m - 1] == 0:
                bfs(i, m - 1)
        for j in range(m):
            if grid[0][j] == 0:
                bfs(0, j)
            if grid[n - 1][j] == 0:
                bfs(n - 1, j)
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0:
                    bfs(i, j)
                    Count += 1
        return Count
