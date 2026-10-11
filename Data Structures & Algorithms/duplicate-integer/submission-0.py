class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for i in range(len(nums)):
            if dup.get(nums[i]) == None:
                dup[nums[i]] = i
            else:
                return True

        return False
            
