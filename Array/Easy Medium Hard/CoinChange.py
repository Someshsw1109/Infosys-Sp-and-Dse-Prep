'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

'''


# Approach/Code - DP, Memoization

# DP Solution
# Memoization
from typing import List


class Solution:
    def MyFunction(self, ind, T, nums, dp):
        if ind == 0:
            if T % nums[0] == 0:
                return T // nums[0]
            return int(1e9)
        if dp[ind][T] != -1:
            return dp[ind][T]
        NotTake = 0 + self.MyFunction(ind - 1, T, nums, dp)
        Take = float('inf')
        if nums[ind] <= T:
            Take = 1 + self.MyFunction(ind, T - nums[ind], nums, dp)
        dp[ind][T] = min(Take, NotTake)
        return dp[ind][T]
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # Memoization
        dp = []
        for i in range(n):
            row = []
            for j in range(amount + 1):
                row.append(-1)
            dp.append(row)
        result = self.MyFunction(n - 1, amount, coins, dp)
        return -1 if result >= int(1e9) else result