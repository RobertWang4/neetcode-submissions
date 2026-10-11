class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        sets = []

        first = nums[0]

        sub = self.subsets(nums[1:])

        for s in sub:
            sets.append(s)
            sets.append(s+[first])

        return sets
