class Solution:
    def longestCommonPrefix(self, strs):
        pre = ""
        for i in range(len(strs[0])):
            for k in range(len(strs)):
                try :
                    if strs[k][i] != strs[0][i]:
                        return pre
                        break
                except:
                    return pre
                    break
            pre += strs[0][i]
        return pre
        