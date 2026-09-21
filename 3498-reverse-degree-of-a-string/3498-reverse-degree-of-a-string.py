class Solution:
    def reverseDegree(self, s: str) -> int:
        ret = 0
        for ind,num in enumerate(s,1):
            print(ind,num)
            ret += ind * (26 - (ord(num) - 97))
        return ret
        