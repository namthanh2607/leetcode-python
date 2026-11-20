
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return 0
        s = [1] * n
        s[0] = 0
        s[1] = 0
        for i in range(2,int(math.sqrt(n)) + 1):
            if s[i] == 1:
                k = 2
                while i * k < n:
                    s[i * k] = 0
                    k += 1
        return sum(s)
        