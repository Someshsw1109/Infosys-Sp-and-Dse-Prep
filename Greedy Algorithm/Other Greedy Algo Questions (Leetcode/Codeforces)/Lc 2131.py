# Leetcode Q.No- 2131 Longest Palindrome by Concatenating Two Letter Words


# Approach -> Greedy Algo

from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        '''
        1-> Check karenge ki dono letter same hai yaa nahi agar nahi hai same to check karenge ki uss list me uska reverse hai yaa nahi i.e, if word is "ab" then we check if "ba" is present in that list or not.
        2-> Agar reverse mil gaya to minimum select karenge from words aur reverse jo hai uska bhi (We will store in a Map)
        3-> Hum isme freq v check karenge aur usse palindrome create karenge aur jiski frequency 1 hai usko hum ekk hi baar use karenge

        '''
        from collections import Counter
        Map = Counter(words)
        res = 0
        Centreused = False
        for word in words:
            if Map[word] == 0:
                continue
            reversedString = word[::-1]
            if reversedString != word:
                if Map[word] > 0 and Map[reversedString] > 0:
                    Map[word] -= 1
                    Map[reversedString] -= 1
                    res += 4
            else:
                if Map[word] >= 2:
                    Map[word] -= 2
                    res += 4
                elif Map[word] == 1 and Centreused == False:
                    Map[word] -= 1
                    res += 2
                    Centreused = True
        return res