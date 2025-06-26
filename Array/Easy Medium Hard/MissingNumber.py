'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

 
 

 

 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?



'''

# Approach (Brute Force) Check every number if not present in array simply return that number

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute Force
        n = len(nums)
        for i in range(0, n + 1):
            if i not in nums:
                return i
            

# Approach (Better) Dictionary

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Using Dictionary
        freq = {}
        n = len(nums)
        for i in range(0, n + 1):
            freq[i] = 0
        for j in nums:
            freq[j] = 1
        for m, n in freq.items():
            if n == 0:
                return m
            

# Approach (Very Simple and optimal) Using Maths

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Using Simple Maths
        # If there is a range given let's say range is 3 then numbers are 0, 1, 2, 3 then we need to calculate the sum of these numbers like 0+1+2+3 = 6, Now we need to calculate the actual sum of input array and we just need to subtract the Actual sum from the above expected sum
        n = len(nums)
        ExpectedSum = (n*(n + 1)) // 2
        ActualSum = sum(nums)
        return ExpectedSum - ActualSum