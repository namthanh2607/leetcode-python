import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        if numRows == 1:
            return s
        else:
            heso = (numRows - 2) * 2 + 2
            for k in range(math.ceil(heso/2) + 1):
                t = heso - k
                for i in range(len(s)):
                    if i % heso == k or i % heso == t:
                        ans = ans + s[i]
        return ans
        