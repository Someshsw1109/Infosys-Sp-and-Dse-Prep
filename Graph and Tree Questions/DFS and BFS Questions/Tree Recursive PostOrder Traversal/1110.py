# Leetcode Q. No- 1110 Delete Nodes And Return Forest


# Using Recursive DFS


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        Set = set(to_delete)
        def dfs(root, Set, res):
            if root is None:
                return None
            root.left = dfs(root.left, Set, res)
            root.right = dfs(root.right, Set, res)
            if root.val in Set:
                if root.left is not None:
                    res.append(root.left)
                if root.right is not None:
                    res.append(root.right)
                return None
            else:
                return root
        dfs(root, Set, res)
        if root.val not in Set:
            res.append(root)
        return res