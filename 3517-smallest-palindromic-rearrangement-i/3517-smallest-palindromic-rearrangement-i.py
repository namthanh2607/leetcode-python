class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) % 2 == 0:
            cur = s[:len(s) // 2]
            lst = []
            for i in cur:
                lst.append(i)
            lst.sort()
            lst = ''.join(lst)
            return lst + lst[::-1]
        cur = s[:len(s) // 2]
        lst = []
        for i in cur:
            lst.append(i)
        lst.sort()
        lst = ''.join(lst)
        return lst + s[len(s)//2] + lst[::-1]
        