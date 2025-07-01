# Leetcode Q No- 105

# Basic Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: # type: ignore
        def Recursive(preorder, inorder, start, end, idx):
            if start > end:
                return None
            rootVal = preorder[idx[0]]
            i = start
            for i in range(end):
                if inorder[i] == rootVal:
                    break
                i += 1
            idx[0] += 1
            root = TreeNode(rootVal) # type: ignore
            root.left = Recursive(preorder, inorder, start, i - 1, idx)
            root.right = Recursive(preorder, inorder, i + 1, end, idx)
            return root
        n = len(preorder)
        idx = [0]
        return Recursive(preorder, inorder, 0, n - 1, idx)