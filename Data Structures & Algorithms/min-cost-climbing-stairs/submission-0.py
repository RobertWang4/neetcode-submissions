class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[0],dp[1] = cost[0],cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2]+cost[i],dp[i-1]+cost[i])
        
        return cost[0] if len(cost) == 1 else min(dp[-1],dp[-2])