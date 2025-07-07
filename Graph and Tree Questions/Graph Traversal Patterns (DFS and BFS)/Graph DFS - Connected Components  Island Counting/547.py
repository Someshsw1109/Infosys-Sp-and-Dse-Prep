# Leetcode Q.No- 547 Number of Provinces


# Using Recursive DFS

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(city):
            for otherCity in range(n):
                if isConnected[city][otherCity] == 1 and otherCity not in visited:
                    visited.add(otherCity)
                    dfs(otherCity)
        count = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        return count
    

# Using bfs

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                queue = [i]
                while queue:
                    city = queue.pop()
                    for otherCity in range(n):
                        if isConnected[city][otherCity] == 1 and otherCity not in visited:
                            visited.add(otherCity)
                            queue.append(otherCity)
                count += 1
        return count