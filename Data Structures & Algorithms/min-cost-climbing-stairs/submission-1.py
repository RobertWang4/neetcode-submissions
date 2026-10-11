class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        a,b = cost[0],cost[1]
        for i in range(2,len(cost)):
            a,b = b,min(a+cost[i],b+cost[i])
        
        return cost[0] if len(cost) == 1 else min(a,b)