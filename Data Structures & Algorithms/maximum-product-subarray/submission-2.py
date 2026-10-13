class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp = nums[0]
        cur_min = nums[0]
        cur_max = nums[0]
        res = nums[0]
        
        for i in range(1,len(nums)):
            n = nums[i]
            temp = cur_max*n
            cur_max = max(n,temp,cur_min*n)
            cur_min = min(n,temp,cur_min*n)
            res = max(res,cur_max)
        return res