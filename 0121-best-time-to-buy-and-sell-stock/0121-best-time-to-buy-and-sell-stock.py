class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        total = [0] * len(prices) 
        total[0] = 0

        for i in range(1,len(prices)):
            total[i] = total[i - 1] + prices[i] - prices[i - 1]
            if total[i] < 0:
                total[i] = 0

        return max(total)