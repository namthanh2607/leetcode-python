class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        check = False
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
        count = 0
        for i in d.values():
            if i % 2 == 1:
                count += i - 1
                check = True
            else:
                count += i
        if check: 
            return count + 1
        return count
        