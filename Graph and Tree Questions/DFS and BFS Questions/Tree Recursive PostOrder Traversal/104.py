# Leetcode Q No- 104 Maximum Depth of Binary Tree

# Using Recursion (DFS)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            LeftSubtree = dfs(node.left)
            RightSubtree = dfs(node.right)
            MaximumCount = max(LeftSubtree, RightSubtree)
            return 1 + MaximumCount
        return dfs(root)