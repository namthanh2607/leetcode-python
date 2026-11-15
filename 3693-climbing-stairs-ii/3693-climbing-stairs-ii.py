class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        try:
            dp[1] = costs[0] + 1
            dp[2] = min(dp[1] + 1, 4) + costs[1]
        except:
            return dp[-1]
        for i in range(3, n + 1):
            dp[i] = min(dp[i-1] + 1, dp[i - 2] + 4, dp[i - 3] + 9) + costs[i - 1]
        print(dp)
        return dp[-1]
        