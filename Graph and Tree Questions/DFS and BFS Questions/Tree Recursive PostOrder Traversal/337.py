# Leetcode Q.No- 337 House Robber III

# Using Recursive Tree DP



# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return [0, 0]
            LeftSubtree = dfs(root.left)
            RightSubtree = dfs(root.right)
            Withroot = root.val + LeftSubtree[1] + RightSubtree[1]
            Withoutroot = max(LeftSubtree) + max(RightSubtree)
            return [Withroot, Withoutroot]
        res = dfs(root)
        return max(res)