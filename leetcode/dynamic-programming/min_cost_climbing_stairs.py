class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        dp = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            next = cost[i] + min(dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = next
        
        return min(dp[0], dp[1])