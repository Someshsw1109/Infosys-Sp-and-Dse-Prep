# Leetcode Q-1161

# Using BFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #  Usinge BFS
        MaximumSum = float('-inf')
        Smallestlevel = 0
        from collections import deque
        q = deque()
        q.append(root)
        CurrentLevel = 1
        while q:
            n = len(q)
            Sum = 0
            while n > 0:
                temp = q.popleft()
                Sum += temp.val
                n -= 1
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            if Sum > MaximumSum:
                MaximumSum = Sum
                Smallestlevel = CurrentLevel
            CurrentLevel += 1
        return Smallestlevel
        