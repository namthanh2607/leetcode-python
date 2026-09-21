class Solution:
    def climbStairs(self, n: int) -> int:
        M = [0] * (n+1)
        if n in [1,2] :
            return n
        else:
            def init():
                M[1] = 1
                M[2] = 2
            def Ans(n):
                if M[n] == 0:
                    M[n] = Ans(n-1) + Ans(n-2)
                return M[n]
            
            init()
            return Ans(n)