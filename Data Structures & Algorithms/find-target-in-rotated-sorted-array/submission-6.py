class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:   
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        if pivot == 0:
            nl = 0
            nr = len(nums) - 1
        elif target >= nums[0]:
            nl = 0
            nr = l - 1
        else:
            nl = l
            nr = len(nums) - 1
        
        while nl <= nr:
            nm = nl + (nr - nl) // 2
            if nums[nm] < target:
                nl = nm + 1
            elif nums[nm] > target:
                nr = nm - 1
            else:
                return nm
        return -1
        