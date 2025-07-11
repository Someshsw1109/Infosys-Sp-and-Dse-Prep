# Leetcode Q.No- 1323 Maximum 69 Number

# Approach -> Greedy Algo

class Solution:
    def maximum69Number (self, num: int) -> int:
        # Approach - 1
        # Jo given integer hai usko list of chars me change kar do
        CharacterNum = list(str(num))
        # Iterate over the entire list
        for i in range(len(CharacterNum)):
            if CharacterNum[i] == '6':
                CharacterNum[i] = '9' # If the Character is '6' replace it with '9'
                break # Because we want only first 6 to replace(I mean jo hume starting me hi pahle mil jaaye)
        return int("".join(CharacterNum))
    
# Approach -> Greedy(But Tricky)

class Solution:
    def maximum69Number (self, num: int) -> int:
        # Approach - 2 (Tricky)
        import math
        placeValue = 0
        placevalueOfSix = -1

        temp = num
        while temp > 0:
            remainder = temp % 10
            if remainder == 6:
                placevalueOfSix = placeValue
            temp = temp // 10
            placeValue += 1
        if placevalueOfSix == -1:
            return num
        return num + 3 * int(math.pow(10, placevalueOfSix))