# Leetcode Q NO- 173


# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSIIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while node is not None:
            self.stack.append(node)
            node = node.left # First we traverse left child of the root
    
    def next(self):
        node = self.stack.pop()
        val = node.val
        node = node.right
        while node is not None:
            self.stack.append(node)
            node = node.left
        return val
    def hasNext(self):
        return bool(self.stack)
    



# Time Complexity: O(1)Amortized, Space Complexity: O(h) where h is the height of the tree
