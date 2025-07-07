# Leetcode Q.No- 652 Find Duplicate Subtrees

# Using Recursive dfs

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        from collections import defaultdict
        Map = defaultdict(int)
        res = []
        def dfs(root, Map, res):
            if root is None:
                return "N"
            S = str(root.val) + "," + dfs(root.left, Map, res) + "," + dfs(root.right, Map, res)
            if Map[S] == 1:
                res.append(root)
            Map[S] += 1
            return S
        dfs(root, Map, res)
        return res