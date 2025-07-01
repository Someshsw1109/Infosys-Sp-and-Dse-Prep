# Leetcode Q.No- 257

# Using Recursive DFS Approach

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Recursive DFS Approach
        ans = []
        def allPaths(root, paths):
            if root is None:
                return
            if paths:
                paths += "->" + str(root.val)
            else:
                paths += str(root.val)
            if root.left is None and root.right is None:
                ans.append(paths)
                return
            if root.left:
                allPaths(root.left, paths)
            if root.right:
                allPaths(root.right, paths)
        allPaths(root, "")
        return ans
            