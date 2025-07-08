# Leetcode Q.No- 733 Flood Fill



# using recursive dfs


from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        oldcolour = image[sr][sc]
        if oldcolour == color:
            return image
        def dfs(row, col):
            if image[row][col] == oldcolour:
                image[row][col] = color
                if row > 0:
                    dfs(row - 1, col)
                if row < m - 1:
                    dfs(row + 1, col)
                if col > 0:
                    dfs(row, col - 1)
                if col < n - 1:
                    dfs(row, col + 1)
        dfs(sr, sc)
        return image
    

# Using BFS

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque
        n = len(image)
        m = len(image[0])
        StartingColor = image[sr][sc]
        if StartingColor == color:
            return image
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            row, col = queue.popleft()
            for x, y in directions:
                a, b = x + row, y + col
                if a >= 0 and a < n and b >= 0 and b < m and image[a][b] == StartingColor:
                    image[a][b] = color
                    queue.append((a, b))
        return image