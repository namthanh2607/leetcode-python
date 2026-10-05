class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        d = triangle
        n = len(d)
        if n == 1:
            return d[0][0]

        for i in range(1,n):
            for j in range(i + 1):
                if j == 0 :
                    d[i][j] += d[i - 1][j]
                elif j == i:
                    d[i][j] += d[i - 1][j - 1]
                else:
                    d[i][j] += min(d[i - 1][j], d[i - 1][j - 1])

        return min(d[-1])

        