# Leetcode Q. No - 530

# Using DFS (Inorder Traversal) But with extra Space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            stack.append(node.val)
            dfs(node.right)
        dfs(root)
        MinDiff = float('inf')
        for i in range(1, len(stack)):
            MinDiff = min(MinDiff, abs(stack[i] - stack[i - 1]))
        return MinDiff



# Using dfs but without extra space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        MinDiff = float('inf')
        def dfs(node):
            nonlocal prev, MinDiff
            if node is None:
                return
            dfs(node.left)
            if prev is not None:
                MinDiff = min(MinDiff, abs(node.val - prev.val))
            prev = node
            dfs(node.right)
        dfs(root)
        return MinDiff