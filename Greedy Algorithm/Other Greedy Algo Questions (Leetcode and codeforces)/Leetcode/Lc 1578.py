# Leetcode Q.No- 1578 Minimum Time to Make Rope Colorful

# Approach -> Greedy

from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors = list(colors)
        n = len(colors)
        time = 0
        Previous_Max = 0
        for i in range(n):
            curr = neededTime[i]
            if i > 0 and colors[i] != colors[i - 1]:
                Previous_Max = 0
            time += min(Previous_Max, curr) # Greedily hum minimum wale ko utha rahe
            Previous_Max = max(Previous_Max, curr)
        return time