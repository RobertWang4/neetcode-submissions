class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def extand(l,r):
            c = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
            return c
        
        for i in range(len(s)):
            count += extand(i,i)
            count += extand(i,i+1)
        
        return count