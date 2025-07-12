# Leetcode Q.No- 991 Broken Calculator

# Approach -> Greedy

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # Agar Start Value target se bara hai yaa barabar hai to simply hum target ko start value se subtract kar denge
        if startValue >= target:
            return startValue - target
        if target % 2 == 0: # Agar target ka value even number hai to hum simply target ko 2 se divide karte jaayenge aur ekk point aisa aayega jahan hum agar phir se 2 se divide karenge to resultant number start value se chota ho jaayega to uss point pe hum +1 kar denge uss value me jo target ke barabar ho jaayega
            return 1 + self.brokenCalc(startValue, target // 2)
        return 1 + self.brokenCalc(startValue, target + 1)