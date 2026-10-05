import math
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = []
        for i in range(rowIndex + 1):
            res.append(math.comb(rowIndex,i))
        return res 
        