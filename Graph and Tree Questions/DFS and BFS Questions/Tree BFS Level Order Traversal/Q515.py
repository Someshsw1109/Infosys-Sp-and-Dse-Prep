# Leetcode Q-515

# Using BFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        ans = []
        if root is None:
            return ans
        from collections import deque
        q = deque([root])
        while q:
            n = len(q)
            MaxElement = float('-inf')
            while n > 0:
                node = q.popleft()
                MaxElement = max(MaxElement, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n -= 1
            ans.append(MaxElement)
        return ans
    


# Using DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # DFS
        res = []
        def dfs(root, depth):
            if root is None:
                return
            if len(res) == depth:
                res.append(root.val)
            else:
                res[depth] = max(res[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return res


# Using DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import defaultdict
        # Using DFS
        Mp = defaultdict(int)
        def DFS(root, level):
            if root is None:
                return
            Mp[level] += root.val
            DFS(root.left, level + 1)
            DFS(root.right, level + 1)
        DFS(root, 1)
        MaxSum = float('-inf')
        resLevel = 0
        for level, Sum in Mp.items():
            if Sum > MaxSum:
                MaxSum = Sum
                resLevel = level
        return resLevel