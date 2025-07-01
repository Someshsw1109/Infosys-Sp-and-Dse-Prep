# Leetcode Q No- 226

# Using Recursion

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive Approach
        if root is None:
            return
        Left = self.invertTree(root.left)
        Right = self.invertTree(root.right)
        root.left = Right
        root.right = Left
        return root
    
# Iterative Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Using BFS
        if root is None:
            return
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            Node = q.popleft()
            Node.left, Node.right = Node.right, Node.left
            if Node.left:
                q.append(Node.left)
            if Node.right:
                q.append(Node.right)
        return root