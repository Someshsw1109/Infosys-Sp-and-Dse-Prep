'''Author - Somesh Raj, Created on 13-07-2025'''

# Codeforces Question - Given Length and Sum of Digits (Rating-1400)

# Greedy Approach 

# Logic : Given Length and Sum of Digits
# Maximum Number ke lie(Greedy): Agar tumhe zyada se zyada number banana hai to sabse pehle digit mein sabse bada number daalo — kyunki leftmost digit ka weight sabse zyada hota hai.
# Minimum Number ke lie : Sabse chhoti digits use karo, par leftmost digit zero nahi hona chahiye.

def Solve(m , s):
    if s == 0 and m > 1 or s > 9*m:
        return "-1", "-1"

    # Maximum Number
    MaxSum = s
    MaxNum = ""
    for _ in range(m):
        digit = min(9, MaxSum) # Minimum Digit
        MaxNum += str(digit) # Maximum Number
        MaxSum -= digit
    
    # Minimum Number
    MinSum = s
    MinNum = ""
    for i in range(m):
        for j in range(0, 10): # To consider all valid digits (0–9)
            if (i > 0 or j > 0 or (m == 1 and j == 0)) and MinSum - j <= (m - i - 1) * 9:
                MinNum += str(j)
                MinSum -= j
                break
    return MinNum, MaxNum

m, s = map(int, input().split())
res = Solve(m, s)
print(*res)

# @Copyright Somesh Raj
