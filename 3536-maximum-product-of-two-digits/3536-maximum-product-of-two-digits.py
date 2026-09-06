class Solution:
    def maxProduct(self, n: int) -> int:
        lst = []
        for i in str(n):
            lst.append(int(i))
        lst.sort(        )
        return lst[-2] * lst[-1]