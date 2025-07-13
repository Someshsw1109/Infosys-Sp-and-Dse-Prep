'''Author - Somesh Raj, Created on 13-07-2025'''

# Codeforces Question - Potions (Hard Version) (Rating-1600)

# Greedy Approach, heap

from heapq import heappop, heappush

def solve(arr):
    health = 0
    MinHeap = []
    # For each potion a[i] in the array
    for i in arr:
        # Drink it: health += a[i]
        health += i
        # Add a[i] to min_heap
        heappush(MinHeap, i)
        # If health < 0
        if health < 0:
            # Remove the potion with lowest effect (most negative) from min_heap
            healthDecreased = heappop(MinHeap)
            health -= healthDecreased
    return len(MinHeap)
n = int(input())
arr = list(map(int, input().split()))
res = solve(arr)
print(res)


# @Copyright Somesh Raj

