# Leetcode Q.No- 2279 Maximum Bags With Full Capacity of Rocks

# Approach - Greedy

from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # Take a required Array in which we store the required rocks to fill the bags
        n = len(capacity)
        requiredArray = []
        for i in range(n):
            currrocks = rocks[i]
            capacityrocks = capacity[i]
            requiredrocks = capacityrocks - currrocks
            requiredArray.append(requiredrocks)
        # Sort that required Array
        requiredArray.sort()
        count = 0
        # Iterate in sorted array and find the result
        for i in range(n):
            if requiredArray[i] == 0:
                count += 1
            else:
                if additionalRocks >= requiredArray[i]:
                    additionalRocks -= requiredArray[i]
                    count += 1
                else:
                    break
        return count