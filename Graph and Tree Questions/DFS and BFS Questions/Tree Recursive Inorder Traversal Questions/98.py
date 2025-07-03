# Leetcode Q. No- 98

#  Using DFS Approach

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    # DFS Approach
    def Check(self, root, Min, Max):
        if root is None:
            return True
        if Min is not None and root.val <= Min.val:
            return False
        if Max is not None and root.val >= Max.val:
            return False
        return self.Check(root.left, Min, root) and self.Check(root.right, root, Max)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.Check(root, None, None)
        
