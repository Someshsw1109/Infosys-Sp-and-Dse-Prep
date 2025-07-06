# Leetcode Q.No- 2458 Height of Binary Tree After Subtree Removal Queries

# Using Inorder DFS

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        level = [0] * 100001
        height= [0] * 100001
        Level_ka_maximum_height = [0] * 100001
        Level_ka_second_maximum_height = [0] * 100001
        # if a node is deleted check other node in the same level and find the maximum height... -- H
        # Find level of the deleted node --- L
        # res = L + H - 1
        def HeightOfTree(root, l):
            nonlocal level, height, Level_ka_maximum_height, Level_ka_second_maximum_height
            if root is None:
                return 0
            level[root.val] = l
            leftheight = HeightOfTree(root.left, l + 1)
            rightheight = HeightOfTree(root.right, l + 1)
            height[root.val] = max(leftheight, rightheight) + 1
            if Level_ka_maximum_height[l] < height[root.val]:
                Level_ka_second_maximum_height[l] = Level_ka_maximum_height[l]
                Level_ka_maximum_height[l] = height[root.val]
            elif Level_ka_second_maximum_height[l] < height[root.val]:
                Level_ka_second_maximum_height[l] = height[root.val]
            return height[root.val]
        HeightOfTree(root, 0)
        res = []
        for node in queries:
            L = level[node]
            temp = L + (Level_ka_second_maximum_height[L] if Level_ka_maximum_height[L] == height[node] else Level_ka_maximum_height[L]) - 1
            res.append(temp)
        return res
