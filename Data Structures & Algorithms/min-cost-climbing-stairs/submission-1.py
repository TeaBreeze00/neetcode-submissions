class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+2)
        # recurrence: max(dp[i+1], dp[i+2])
        # We can start take the min of either starting from 0 or from 1
        for i in range(len(cost) - 1, -1, -1):
            dp[i] = min(cost[i]+dp[i+1], cost[i]+dp[i+2])

        return min(dp[0], dp[1])    