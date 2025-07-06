# Leetcode Q.No- 863 All Nodes Distance K in Binary Tree

# Using parent pointer, BFS

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import deque
        parent = {}
        def inorder(root):
            nonlocal parent
            if root is None:
                return
            if root.left is not None:
                parent[root.left] = root
            inorder(root.left)
            if root.right is not None:
                parent[root.right] = root
            inorder(root.right)
        def bfs(target, k, res):
            queue = deque()
            queue.append(target)
            visited = set()
            visited.add(target)
            while queue:
                n = len(queue)
                if k == 0:
                    break
                while n > 0:
                    curr = queue.popleft()
                    if curr.left and curr.left not in visited:
                        queue.append(curr.left)
                        visited.add(curr.left)
                    if curr.right and curr.right not in visited:
                        queue.append(curr.right)
                        visited.add(curr.right)
                    if curr in parent and parent[curr] not in visited:
                        queue.append(parent[curr])
                        visited.add(parent[curr])
                    n -= 1
                k -= 1
            while queue:
                temp = queue.popleft()
                res.append(temp.val)
        res = []
        inorder(root)
        bfs(target, k, res)
        return res