class Solution:
    def addDigits(self, num: int) -> int:
        ret = 0
        for i in str(num):
            ret += int(i)
        if ret >= 10:
            return self.addDigits(ret)
        return ret