class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        prev1 = 1
        prev2 = 1
        
        for i in range(1,len(s)):
            cur = 0

            if s[i] != "0":
                cur += prev1

            if s[i-1] == "1" or (s[i-1] == "2" and s[i] in "0123456"):
                cur += prev2
            
            prev2, prev1 = prev1, cur
        
        return prev1