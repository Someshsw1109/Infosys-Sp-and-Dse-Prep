# Leetcode Q. No- 2101 Detonate the Maximum Bombs

# Using Recursive DFS

from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        from collections import defaultdict
        Map = defaultdict(list)
        n = len(bombs)
        # Check karenge ki agar bomb ka radius dono bomb ke bich ke distance se bara hai yaa equal hai to Map me hum usko append kar denge 
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1 = bombs[i][0] # X coordinate of first bomb
                y1 = bombs[i][1] # Y coordinate of first bomb
                r1 = bombs[i][2] # Radius of first bomb
                x2 = bombs[j][0] # X coordinate of Second bomb
                y2 = bombs[j][1] # Y coordinate of Second bomb
                r2 = bombs[j][2] # Radius of Second bomb
                import math
                Dono_Bomb_ke_bich_ka_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if r1 >= Dono_Bomb_ke_bich_ka_distance:
                    Map[i].append(j)
        def dfs(u, visited, Map):
            visited.add(u)
            for v in Map[u]:
                if v not in visited:
                    dfs(v, visited, Map)
        res = 0
        for i in range(n):
            visited = set()
            dfs(i, visited, Map)
            count = len(visited)
            res = max(res, count)
        return res