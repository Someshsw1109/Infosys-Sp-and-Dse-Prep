# Leetcode Q.No- 881 Boats to Save People


# Approach -> Greedy 

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        NumberOfBoats = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[j] + people[i] <= limit: # Jo sabse halka hoga aur jo sabse bhari hoga dono ke weight ka sum check karenge ki limit ke barabar hai yaa nahi...
                i += 1
                j -= 1
                NumberOfBoats += 1 
            else:
                j -= 1     # Agar upar wala condition false ho gaya to hum jo sabse bhaari hoga usko hum bhej denge (Greedy Approach)
                NumberOfBoats += 1
        return NumberOfBoats