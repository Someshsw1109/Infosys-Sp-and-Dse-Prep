# Leetcode Q.No- 948 Bag Of Tokens

# Approach -> Greedy Algo

from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        MaxScore = 0
        Score = 0
        i = 0
        j = len(tokens) - 1
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                Score += 1
                MaxScore = max(MaxScore, Score)
                i += 1
            elif Score >= 1:
                power += tokens[j]
                Score -= 1
                j -= 1
            else:
                return MaxScore
        return MaxScore