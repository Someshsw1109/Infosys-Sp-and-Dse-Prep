# Leetcode Q No- 988

# Using DFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Using DFS
        res = ""
        def dfs(root, curr):
            nonlocal res
            if root is None:
                return
            curr = chr(root.val + ord('a')) + curr
            if root.left is None and root.right is None:
                if res == "" or res > curr:
                    res = curr
                return
            dfs(root.left, curr)
            dfs(root.right, curr)
        dfs(root, "")
        return res