# Leetcode Q.No- 130 - Surrounded Regions



from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(row, col):
            vis[row][col] = 1
            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and board[nrow][ncol] == 'O':
                    dfs(nrow, ncol)

        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        vis = [[0] * m for _ in range(n)]
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        for j in range(m):
            if board[0][j] == 'O' and not vis[0][j]:
                dfs(0, j)
            if board[n - 1][j] == 'O' and not vis[n - 1][j]:
                dfs(n - 1, j)
        for i in range(n):
            if board[i][0] == 'O' and not vis[i][0]:
                dfs(i, 0)
            if board[i][m - 1] == 'O' and not vis[i][m - 1]:
                dfs(i, m - 1)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not vis[i][j]:
                    board[i][j] = 'X'