
import math
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        dp = [0]*len(arr)
        dp[0] = arr[0] % 2
        for i in range(1,len(arr)):
            if not arr[i] % 2:
                dp[i] = dp[i-1]
            else:
                dp[i] = 1 - dp[i-1]
        odd = sum(dp)
        even = len(dp) - sum(dp)

        ret1 = comb(odd,2)
        ret2 = comb(even,2) + even
        

        return  (comb(len(arr),2) + len(arr) - (ret1 + ret2)) % (10**9+7)