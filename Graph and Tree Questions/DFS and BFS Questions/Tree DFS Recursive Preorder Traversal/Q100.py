# Leetcode q - 100

# Using recursion

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive Approach
        def myFunction(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            return (myFunction(root1.left, root2.left) and myFunction(root1.right, root2.right))
        return myFunction(p, q)

# Using BFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Using BFS
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        from collections import deque
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)
        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if node1.val != node2.val:
                return False
            if node1.left is not None and node2.left is not None:
                q1.append(node1.left)
                q2.append(node2.left)
            elif node1.left is not None or node2.left is not None:
                return False
            if node1.right is not None and node2.right is not None:
                q1.append(node1.right)
                q2.append(node2.right)
            elif node1.right is not None or node2.right is not None:
                return False
        return True