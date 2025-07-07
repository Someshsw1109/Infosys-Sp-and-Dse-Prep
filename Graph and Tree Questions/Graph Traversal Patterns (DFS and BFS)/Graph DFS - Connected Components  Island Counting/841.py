# Leetcode Q.No- 841 Keys and Rooms

# Using Recursive DFS

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        m = len(rooms)
        visited = set()
        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for i in rooms[room]:
                dfs(i)
        dfs(0)
        if len(visited) == m:
            return True
        else:
            return False