class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)

        if int(s[0]) != 0:
            dp[0] = 1

        if len(s) == 1:
            return dp[0]

        if s[0] == '0':
            return 0

        if 10 <= int(s[:2]) <= 26 and s[1] !="0":
            dp[1] = 2
        elif 10 <= int(s[:2]) <= 26 and s[1] == "0":
            dp[1] = 1
        elif s[1] != '0':
            dp[1] = 1

        for i in range(2,len(s)):
            if 1 <= int(s[i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]

            if dp[i] == 0:
                return 0
            
        print(dp)
        
        return dp[-1]


        
        