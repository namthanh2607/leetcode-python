class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        if n == 1:
            return costs[0] + 1

        dp0 = 0
        dp1 = costs[0] + 1
        dp2 = min(dp1 + 1, dp0 + 4) + costs[1]
        
        for i in range(3, n + 1):
            curr = min(dp2 + 1, dp1 + 4, dp0 + 9) + costs[i - 1]
            dp0, dp1, dp2 = dp1, dp2, curr
            
        return dp2