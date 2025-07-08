# Leetcode Q.No- 1020 Number of Enclaves


# Using Recursive DFS

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        Count = 0
        def dfs(row, col):
            nonlocal rows, cols, directions
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
                return
            grid[row][col] = 0
            for x, y in directions:
                dfs(row + x, col + y)
        for i in range(rows):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][cols - 1] == 1:
                dfs(i, cols - 1)
        for j in range(cols):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[rows - 1][j] == 1:
                dfs(rows - 1, j)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # dfs(i, j)
                    Count += 1
        return Count
    


# Using BFS

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        Count = 0
        def bfs(row, col):
            nonlocal rows, cols, directions
            from collections import deque
            queue = deque()
            queue.append((row, col))
            grid[row][col] = 0
            while queue:
                a, b = queue.popleft()
                for x, y in directions:
                    L, R = a + x, b + y
                    if L >= 0 and L < rows and R >= 0 and R < cols and grid[L][R] == 1:
                        grid[L][R] = 0
                        queue.append((L, R))
        for i in range(rows):
            if grid[i][0] == 1:
                bfs(i, 0)
            if grid[i][cols - 1] == 1:
                bfs(i, cols - 1)
        for j in range(cols):
            if grid[0][j] == 1:
                bfs(0, j)
            if grid[rows - 1][j] == 1:
                bfs(rows - 1, j)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # dfs(i, j)
                    Count += 1
        return Count