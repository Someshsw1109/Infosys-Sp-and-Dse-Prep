'''Author - Somesh Raj, Created on 13-07-2025'''

# Codeforces Question - Linova and Kingdom (Rating-1600)

# DFS Approach, Greedy

# Write DFS Function 

import sys
sys.setrecursionlimit(2 * 10**5 + 10)
def dfs(u, node, d):
    SubtreeSize[u] = 1
    depth[u] = d
    for v in graph[u]:
        if v != node:
            dfs(v, u, d + 1)
            SubtreeSize[u] += SubtreeSize[v]
# Input/ Make Graph

n, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
SubtreeSize = [0] * (n + 1)
depth = [0] * (n + 1)
dfs(1, 0, 0) # Because 1 is capital

values = []
for i in range(1, n + 1):
    values.append(depth[i] - SubtreeSize[i] + 1)

values.sort(reverse=True)
Sum = sum(values[:k])
print(Sum)


# @Copyright Somesh Raj