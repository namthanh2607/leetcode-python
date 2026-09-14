import math
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        de_a, de_b = 0, 0
        for i in range(len(a)):
            de_a += 2**(len(a) - 1 - i)*int(a[i])
        for i in range(len(b)):
            de_b += 2**(len(b) - 1 - i)*int(b[i])
        ans = de_a + de_b
        if ans == 0:
            return '0'
        ret = ''
        end = int(math.floor(math.log(ans,2)))
        for i in range(end + 1):
            if ans >= 2**(end - i):
                ret += '1'
                ans -= 2**(end - i)
            else:
                ret+='0'
        return ret




        
            
        


        