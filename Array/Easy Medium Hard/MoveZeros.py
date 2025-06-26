'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

'''

# Approach: Two Pointers - to move all zeros to the end of the array while maintaining the relative order of non-zero elements.

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums:
            if i != 0:
                nums[count] = i
                count += 1
        for i in range(count, len(nums)):
            nums[i] = 0


# Approach: Two Pointers again but this time with different logic

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We take two pointers, i and j, set i and j both at the starting position, then we need to move only j towards the end of the array(traversing) and if j is non zero element then swap it with i and if it's zero then j will move forward....
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1