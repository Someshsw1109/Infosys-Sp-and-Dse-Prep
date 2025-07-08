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



# Using BFS

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        m = len(rooms)
        visited = {0}
        queue = deque()
        queue.append(0)
        while queue:
            KickedRoom = queue.popleft()
            for keys in rooms[KickedRoom]:
                if keys not in visited:
                    visited.add(keys)
                    queue.append(keys)
        return len(visited) == m