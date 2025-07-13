'''Author - Somesh Raj, Created on 13-07-2025'''

# Codeforces Question - Maximum Medians (Rating-1400)

# Greedy Approach, Binary Search

def Solve(n, k, arr):
    # Sort the array
    arr.sort()
    low = arr[n // 2]
    high = low + k
    res = low
    # Binary Search on Median Value
    while low <= high:
        mid = (low + high) // 2
        OperationsNeeded = 0
        # Calculate required operations from Median (n // 2) to end (n)
        for i in range(n // 2, n):
            if arr[i] < mid:
                OperationsNeeded += mid - arr[i]
        # if total operations <= k then we found our answer
        if OperationsNeeded <= k:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = Solve(n, k, arr)
print(ans)

# @Copyright Somesh Raj