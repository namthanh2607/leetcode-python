class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    if j != len(needle) - 1:
                        continue
                    else:
                        return i
                else:
                    break
        return -1

                

            
        