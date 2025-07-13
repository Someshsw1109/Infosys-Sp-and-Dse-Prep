'''Author - Somesh Raj, Created on 13-07-2025'''

# Codeforces Question - Exams (Rating-1400)

# Greedy Approach

def Solve(n , exams):
# Logic : exams.sort by ai in ascending order
    # def SortBya(exam):
    #     return exam[0]
    # exams.sort(key=SortBya, reverse=True)
    exams.sort(key=lambda x: (x[0], x[1]))
    LastDayCount = 0 # Track last day
    for i, j in exams: # For each exam: try to take it on j if possible, otherwise i
        # scheduled date - i, early date - j
        if j >= LastDayCount:
            LastDayCount = j
        else:
            LastDayCount = i
    return LastDayCount

n = int(input())
exams = [tuple(map(int, input().split())) for _ in range(n)]
res = Solve(n, exams)
print(res)

# @Copyright Somesh Raj

