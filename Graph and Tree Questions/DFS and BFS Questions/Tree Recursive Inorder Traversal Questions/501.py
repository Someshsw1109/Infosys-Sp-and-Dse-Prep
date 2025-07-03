# Leetcode Q.No- 501

# Using Unordered Map

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict
        Map = defaultdict(int)
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            Map[node.val] += 1
            dfs(node.right)
        dfs(root)
        res = []
        MaxFreq = 0
        for key, val in Map.items():
            if val > MaxFreq:
                MaxFreq = val
                res = []
                res.append(key)
            elif val == MaxFreq:
                res.append(key)
        return res
    

# Another Approach Using DFS also this time but with O(1) Space 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.CurrentElement = 0
        self.maxFreq = 0
        self.currFreq = 0
        self.res = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            if self.CurrentElement == node.val:
                self.currFreq += 1
            else:
                self.CurrentElement = node.val
                self.currFreq = 1
            if self.currFreq > self.maxFreq:
                self.res = [node.val]
                self.maxFreq = self.currFreq
            elif self.currFreq == self.maxFreq:
                self.res.append(node.val)
            dfs(node.right)
        dfs(root)
        return self.res
