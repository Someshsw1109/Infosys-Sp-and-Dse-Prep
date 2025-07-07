# Leetcode Q. No- 200 - Number of Islands

from typing import List


# Using Recursive DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for i in range(m)
        # for j in range(n)
        # if grid[i][j] == 1: dfs(grid, i, j)
        Count = 0
        if grid is None:
            return 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        def dfs(a, b):
            nonlocal m, n, grid
            if a < 0 or a >= m or  b < 0 or b >= n or grid[a][b] != '1':
                return
            grid[a][b] = '@'
            for x, y in self.directions:
                dfs(a + x, b + y)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    Count += 1
        return Count


# Using BFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for i in range(m)
        # for j in range(n)
        # if grid[i][j] == 1: dfs(grid, i, j)
        from collections import deque
        if grid is None:
            return 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        Count = 0
        queue = deque()
        
        def bfs(a, b):
            queue.append((a, b))
            grid[a][b] = '@'
            while queue:
                i, j = queue.popleft()
                for x, y in self.directions:
                    p = i + x
                    q = j + y
                    if p >= 0 and p < m and q >= 0 and q < n and grid[p][q] =='1':
                        queue.append((p, q))
                        grid[p][q] = '@'
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    Count += 1
        return Count