class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0

        for right in range(len(s)):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, len(seen))
        
        return max_len

        
