class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        while left < right:
            mid = left + ((right - left) // 2)
            kh = 0
            for p in piles:
                kh += math.ceil(p/mid)
            if kh <= h:
                right = mid
            else:
                left = mid + 1
        return left
