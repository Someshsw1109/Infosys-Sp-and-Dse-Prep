# Leetcode Q.No- 230


# Approach / Code Using Stack
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = root
        stack = []
        nodes = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                nodes.append(node.val)
                node = node.right
        return nodes[k - 1]