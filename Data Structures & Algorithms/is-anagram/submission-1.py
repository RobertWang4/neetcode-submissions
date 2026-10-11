class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = list(s)
        chart = list(t)
        chars.sort()
        chart.sort()

        for i in range(len(chars)):
            if chars[i] != chart[i]:
                return False
        
        return True