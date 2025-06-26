'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000


'''

# Approach/Code (Optimal Solution)

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        Prod1 = nums[n - 1] * nums[n - 2] * nums[n - 3] # Products of three largest number, we can get these numbers from the last index
        Prod2 = nums[0] * nums[1] * nums[n - 1] # If there is negative number then we follow this formulae to calculate the largest product
        return max(Prod1, Prod2) # Find the max product