class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for i in range(2,numRows + 1):
            cur = [1]
            for j in range(i - 2):
                cur.append(res[-1][j] + res[-1][j + 1])
            cur += [1]
            res.append(cur[::])
        return res

        