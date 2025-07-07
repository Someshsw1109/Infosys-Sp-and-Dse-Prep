# Leetcode Q.No- 417 - Pacific Atlantic Water Flow


# Using Recursive DFS

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        res = []
        pacific = set()
        atlantic = set()
        def dfs(rows, cols, vis, previousheight):
            if ((rows, cols) in vis or rows < 0 or cols < 0 or rows == n or cols == m or heights[rows][cols] < previousheight):
                return
            vis.add((rows, cols))
            dfs(rows + 1, cols, vis, heights[rows][cols])
            dfs(rows - 1, cols, vis, heights[rows][cols])
            dfs(rows, cols + 1, vis, heights[rows][cols])
            dfs(rows, cols - 1, vis, heights[rows][cols])
        for i in range(m):
            dfs(0, i, pacific, heights[0][i])
            dfs(n - 1, i, atlantic, heights[n - 1][i])
        for j in range(n):
            dfs(j, 0, pacific, heights[j][0])
            dfs(j, m - 1, atlantic, heights[j][m - 1])
            
        for i in range(n):
            for j in range(m):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append((i, j))
        return res


# Using BFS 


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        n, m = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific = deque()
        atlantic = deque()
        pacificset = set()
        atlanticset = set()
        def bfs(queue, vis):
            nonlocal directions
            while queue:
                rows, cols = queue.popleft()
                for x, y in directions:
                    row, col = rows + x, cols + y
                    if row >= 0 and row < n and col >= 0 and col < m and (row, col) not in vis and heights[row][col] >= heights[rows][cols]:
                        vis.add((row, col))
                        queue.append((row, col))
        for i in range(m):
            pacific.append((0, i))
            pacificset.add((0, i))
            atlantic.append((n - 1, i))
            atlanticset.add((n - 1, i))
        for i in range(n):
            pacific.append((i, 0))
            pacificset.add((i, 0))
            atlantic.append((i, m - 1))
            atlanticset.add((i, m - 1))
        bfs(pacific, pacificset)
        bfs(atlantic, atlanticset)
        res = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pacificset and (i, j) in atlanticset:
                    res.append([i, j])
        return res
