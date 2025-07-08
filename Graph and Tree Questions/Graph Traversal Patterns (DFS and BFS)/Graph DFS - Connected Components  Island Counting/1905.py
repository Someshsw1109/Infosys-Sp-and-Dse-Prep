# Leetcode Q.No- 1905 Count Sub Islands

# Using Recursive DFS

from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])
        p = len(grid2)
        q = len(grid2[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        Count = 0
        def dfs(row, col):
            nonlocal is_Sub
            if row < 0 or row >= n  or col < 0 or col >= m or grid2[row][col] == 0:
                return
            if grid1[row][col] == 0:
                is_Sub = False
            grid2[row][col] = 0
            for x, y in directions:
                dfs(row + x, col + y)
        for i in range(p):
            for j in range(q):
                if grid2[i][j] == 1:
                    is_Sub = True
                    dfs(i, j)
                    if is_Sub:
                        Count += 1
        return Count
                


# Using BFS


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])
        p = len(grid2)
        q = len(grid2[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        Count = 0
        def bfs(row, col):
            nonlocal is_Sub, directions
            from collections import deque
            queue = deque()
            queue.append((row, col))
            grid2[row][col] = 0
            while queue:
                r, c = queue.popleft()
                if grid1[r][c] == 0:
                    is_Sub = False
                for x, y in directions:
                    newrow, newcol = r + x, c + y
                    if newrow >= 0 and newrow < n and newcol >= 0 and newcol < m and grid2[newrow][newcol] == 1:
                        if grid1[newrow][newcol] == 0:
                            is_Sub = False
                        grid2[newrow][newcol] = 0
                        queue.append((newrow, newcol))
        for i in range(p):
            for j in range(q):
                if grid2[i][j] == 1:
                    is_Sub = True
                    bfs(i, j)
                    if is_Sub:
                        Count += 1
        return Count
                