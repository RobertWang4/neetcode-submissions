class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robbery(l,r):
            a,b = 0,0
            for i in range(l,r):
                a, b = b,max(b,a+nums[i])
                
            return max(a,b)
        return max(robbery(0,len(nums)-1),robbery(1,len(nums)))
