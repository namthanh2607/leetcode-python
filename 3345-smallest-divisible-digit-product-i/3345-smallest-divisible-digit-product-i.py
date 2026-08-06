class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(n):
            ans = 1
            for i in str(n):
                ans = ans*int(i)
            return ans

        while check(n) % t != 0:
            n += 1
        return n
        