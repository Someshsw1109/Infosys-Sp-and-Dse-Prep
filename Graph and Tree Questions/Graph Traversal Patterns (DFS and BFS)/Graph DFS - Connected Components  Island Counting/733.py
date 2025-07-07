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