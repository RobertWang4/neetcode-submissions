class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            d = target - nums[i]

            if d in s:
                return [s.get(d),i]
            
            s[nums[i]] = i