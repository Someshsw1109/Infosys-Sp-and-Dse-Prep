# Leetcode Q.No- 2244 Minimum Rounds to Complete All Tasks

# Approach - Grredy


from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # Bahut Simple hai agar hum number of 3x, 3x+1, 3x+2 ke form me likhenge to hume ek pattern mil jaayega and hence uske bdd check karenge ki agar count % 3 == 0 hai to rounds me hum count // 3 add kar denge nahi to hum rounds me count // 3 + 1 add kar denge 
        from collections import Counter
        Map = Counter(tasks)
        rounds = 0
        for count in Map.values():
            if count == 1:
                return -1
            if count % 3 == 0:
                rounds += (count // 3)
            else:
                rounds += (count // 3) + 1
        return rounds