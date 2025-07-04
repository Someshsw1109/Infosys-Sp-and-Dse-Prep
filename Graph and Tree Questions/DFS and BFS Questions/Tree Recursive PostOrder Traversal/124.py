# Leetcode Q.No- 124 Binary Tree Maximum Path Sum

# Using Recursion dfs

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def dfs(node):
            nonlocal maxSum
            if node is None:
                return 0
            left_ka_sum = dfs(node.left)

            right_ka_sum = dfs(node.right)

            Humara_ans_left_aur_right_se_hi_mil_gaya = left_ka_sum + right_ka_sum + node.val

            agar_sirf_root_hi_best_ans_hai = node.val

            agar_inme_Se_koi_ekk_acha_Sum_hai = max(left_ka_sum, right_ka_sum) + node.val

            maxSum = max(maxSum, Humara_ans_left_aur_right_se_hi_mil_gaya, agar_sirf_root_hi_best_ans_hai, agar_inme_Se_koi_ekk_acha_Sum_hai)


            # We can not return the left_right_sum here because when we got the sum through left and right then we don't need to traverse anymore in the tree
            return max(agar_sirf_root_hi_best_ans_hai, agar_inme_Se_koi_ekk_acha_Sum_hai)
        dfs(root)
        return maxSum