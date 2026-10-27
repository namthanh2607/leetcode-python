class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ret = ["." * n] 
        for i in range(m - 1):
            ret.append("#" * (n - 1) + ".")
        return ret

        