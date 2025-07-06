# Leetcode Q.No- 572 Subtree of Another Tree

# Using Recursive DFS

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            LeftIdentical = dfs(root.left, subRoot.left)
            RightIdentical = dfs(root.right, subRoot.right)
            return (root.val == subRoot.val) and LeftIdentical and RightIdentical
        if root is None:
            return False
        if dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)