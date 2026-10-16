class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left = 0
        max_diff = 0

        for right in range(1,len(prices)):
            if prices[right] < prices[left]:
                left = right
                continue
            max_diff = max(max_diff, prices[right]-prices[left])

        return max_diff
