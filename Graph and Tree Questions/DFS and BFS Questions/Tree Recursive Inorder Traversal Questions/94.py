# Leetcode Q-No: 94

# Using Recursive Approach

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive Approach
        if root is None:
            return []
        LeftValue = self.inorderTraversal(root.left)
        CurrValue = [root.val]
        RightValue = self.inorderTraversal(root.right)
        return LeftValue + CurrValue + RightValue



# Using Morris Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Morris Traversal
        res = []
        Curr = root
        while Curr is not None:
            if Curr.left is None:
                res.append(Curr.val)
                Curr = Curr.right
            else:
                LeftChild = Curr.left
                while LeftChild.right is not None:
                    LeftChild = LeftChild.right
                LeftChild.right = Curr
                Temp = Curr
                Curr = Curr.left
                Temp.left = None
        return res
