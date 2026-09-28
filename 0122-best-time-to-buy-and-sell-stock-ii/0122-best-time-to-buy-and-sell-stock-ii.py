class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        total = [0] * len(prices)
        total[0] = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                total[i] = total[i-1] + prices[i] - prices[i-1]
            else:
                total[i] = total[i - 1]
        return total[-1]