# leetcode Q.No- 695 Max Area of Island


# Using Recursive DFS

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row, col):
            nonlocal rows, cols
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            area = 1
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)
            return area
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area


# Using bfs

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            grid[row][col] = 0
            area = 1
            nonlocal rows, cols, directions
            while queue:
                row, col = queue.popleft()
                for x, y in directions:
                    a, b = row + x, col + y
                    if a >= 0 and a < rows and b >= 0 and b < cols and grid[a][b] == 1:
                        grid[a][b] = 0
                        queue.append((a, b))
                        area += 1
            return area       
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
        return max_area