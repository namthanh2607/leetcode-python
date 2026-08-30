class Solution:
    def checkDivisibility(self, n: int) -> bool:
        pro = 1
        cur = 0
        for i in str(n):
            cur += int(i)  
            pro *= int(i)
        if n % (cur + pro)  == 0:
            return True
        return False