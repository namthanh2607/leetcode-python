import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        ret = 0
        for i in range(k + 1, 2 * k + 1):
            ret += math.comb(n, i)* math.comb(k - 1, 2 * k - i)
        return ret % (10**9 + 7)