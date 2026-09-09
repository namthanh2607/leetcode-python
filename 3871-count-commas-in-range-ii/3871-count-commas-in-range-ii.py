class Solution:
    def countCommas(self, n: int) -> int:
        leng = len(str(n))
        comma = (leng - 1) // 3
        if comma == 0 :
            return 0
        ret = 0 
        for i in range(1,comma + 1):
            ret += n - int("999" * i)
        return ret

        

        