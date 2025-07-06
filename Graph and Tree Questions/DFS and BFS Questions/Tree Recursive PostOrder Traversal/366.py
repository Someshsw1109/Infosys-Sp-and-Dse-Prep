# Leetcode Q.No- 366 Find Leaves of Binary Tree, It's a Premium Question


# Logic : calculate the height of each node using postorder DFS, group all nodes with the same height, Leaves get the lowest height and are grouped together in the result.

from typing import List, Optional


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        from collections import defaultdict
        Map = defaultdict(list)
        res = []
        def heightofthetree(root):
            nonlocal Map
            if root is None:
                return 0
            LeftHeight = heightofthetree(root.left)
            RightHeight = heightofthetree(root.right)
            HeightFothetree = 1 + max(LeftHeight, RightHeight)
            Map[HeightFothetree].append(root.val)
            return HeightFothetree
        heightofthetree(root)
        for key in Map:
            res.append(Map[key])
        return res
