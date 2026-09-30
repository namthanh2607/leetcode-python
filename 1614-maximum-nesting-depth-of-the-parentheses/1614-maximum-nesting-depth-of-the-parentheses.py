class Solution:
    def maxDepth(self, s: str) -> int:
        ret = 0
        count = 0
        for i in s:
            if i == "(":
                count += 1
                if ret < count:
                    ret = count
            if i == ")":
                count -= 1
        return ret
