# Leetcode Q.No- 543 Diameter of Binary Tree


# Using Recursive DFS Approach

from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # type: ignore
        # Using Recursive dfs
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            Left = dfs(node.left)
            Right = dfs(node.right)
            res = max(res, Left + Right)
            return max(Left, Right) + 1
        dfs(root)
        return res
            