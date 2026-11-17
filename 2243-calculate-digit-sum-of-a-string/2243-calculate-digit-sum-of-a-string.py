class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            cur = ''
            for i in range(len(s)//k):
                cur += str(sum(int(x) for x in s[k*i: k*i + k]))
            if k*i + k < len(s):
                cur += str(sum(int(x) for x in s[k*i + k:]))
            s = cur
        return s
        