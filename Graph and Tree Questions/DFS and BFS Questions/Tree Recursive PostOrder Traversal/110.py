# Leetcode Q.No- 110

# Simple DFS Recursive Approach

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: # type: ignore
        def dfs(node):
            if node is None:
                return 0
            LeftHeight = dfs(node.left)
            if LeftHeight == -1:
                return -1
            RightHeight = dfs(node.right)
            if RightHeight == -1:
                return -1
            if abs(LeftHeight - RightHeight) > 1:
                return -1
            return 1 + max(LeftHeight, RightHeight)
        return dfs(root) != -1