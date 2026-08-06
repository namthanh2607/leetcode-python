class Solution:
    def longestPalindrome(self, s: str) -> str:


        sub = ""
        if len(s) == 1 or len(s) == 0:
            return s
        else:
            for t in range(0,len(s)):
                sub_now = s[t]
                left = t - 1
                right = t + 1
                while left >= 0  and right <= len(s)-1 and s[left] == s[right]:
                    left = left - 1
                    right = right + 1
                sub_now = s[left+1:right]    
                if len(sub_now) > len(sub) :
                    sub = sub_now
            for t in range(0,len(s)):
                sub_now = ""
                left = t - 1
                right = t
                while left >= 0  and right <= len(s)-1 and s[left] == s[right]:
                    left = left - 1
                    right = right + 1
                sub_now = s[left+1:right]    
                if len(sub_now) > len(sub) :
                    sub = sub_now
                    
        return sub