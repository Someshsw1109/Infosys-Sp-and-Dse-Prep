# Leetcode Q.No- 2136 Earliest Possible Day of Full Bloom (Seriously It's a very Good Question)

# Using Greedy Algo

from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)

        # Create a List and append the ith value of plant time and grow time
        plants = []
        for i in range(n):
            plants.append((plantTime[i], growTime[i]))

        def Grow(plant):
            return plant[1]

        plants.sort(key=Grow, reverse=True)  # Sort it in descending order according to your own choice

        MaxDayForBloom = 0
        PrevPlantDays = 0
        for i in range(n):
            # Find the current grow and current plant time
            CurrentPlantTime = plants[i][0] # EveryTime you start planting your first seed it will take 1 day
            CurrentGrowTime = plants[i][1] # Grow time is the next index of the last day of planting a seed
            PrevPlantDays += CurrentPlantTime
            CurrentBloomTime = CurrentGrowTime + PrevPlantDays
            MaxDayForBloom = max(MaxDayForBloom, CurrentBloomTime)
        return MaxDayForBloom