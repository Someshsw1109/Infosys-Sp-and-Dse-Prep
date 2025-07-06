# Leetcode Q.No- 235 Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        LeftAncestor = self.lowestCommonAncestor(root.left, p, q)
        RightAncestor = self.lowestCommonAncestor(root.right, p, q)
        if LeftAncestor is not None and RightAncestor is not None:
            return root
        if LeftAncestor is not None:
            return LeftAncestor
        return RightAncestor