class Solution:
    def jump(self, nums: List[int]) -> int:
        start = 0
        end = 0
        max_end = 0
        steps = 0

        while max_end < len(nums) - 1:
            for i in range(start, end+1):
                max_end = max(max_end,i+nums[i])
            
            start = end+1
            end = max_end
            steps += 1
        return steps

