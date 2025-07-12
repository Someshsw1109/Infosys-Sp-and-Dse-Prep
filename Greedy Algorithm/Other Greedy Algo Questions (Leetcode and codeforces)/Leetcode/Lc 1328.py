# Leetcode Q.No- 1328 Break a Palindrome


# Approach -> Greedy

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome) # First hum string ko list me convert kar lenge jisse hume traverse karne me aasani hoga
        n = len(palindrome)
        if n <= 1: # Agar length 1 se chota hai to obviously hum empty string return karenge according to the question
            return ""
        for i in range(n//2): # Agar length even hai then hume pura traverse karne ki need nahi hai agar hum half length tak v travel kar krke koi char ko change kar denge to wo palindrome ko break kar dega
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return "".join(palindrome)
        palindrome[n - 1] = 'b' # Agar length odd hai to list me jo sbse last element hai usko replace kar denge b se
        return "".join(palindrome)