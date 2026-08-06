class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = 0
        sub = ""
        for i in range(len(s)):
            if s[i] not in sub:
                sub += s[i]
            else:
                posi = sub.find(s[i])
                sub = sub[posi + 1 :] + s[i]
            long = max(long,len(sub))
        return long
                    
                    