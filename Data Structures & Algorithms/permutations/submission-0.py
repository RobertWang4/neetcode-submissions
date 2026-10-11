class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        used = set()

        def dfs():
            if len(sub) >= len(nums):
                res.append(sub.copy())
                return
            
            for n in nums:
                if n in used:
                    continue
                sub.append(n)
                used.add(n)
                dfs()
                sub.pop()
                used.remove(n)
        
        dfs()
        return res
