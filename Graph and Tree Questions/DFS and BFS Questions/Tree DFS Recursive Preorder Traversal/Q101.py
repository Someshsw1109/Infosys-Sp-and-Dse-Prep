# Leetcode Q No- 100

# Recursive Approach

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(Left, Right):
            if Left is None and Right is None:
                return True
            if Left is None or Right is None:
                return False
            if Left.val == Right.val and check(Left.left, Right.right) and check(Left.right, Right.left):
                return True
            return False
        if root is None:
            return True
        return check(root.left, root.right)