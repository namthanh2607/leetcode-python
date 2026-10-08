class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        cout = 0
        start = 0
        end = 0
        for i in range(len(s)):
            if i >= 1:
                end += 1

            if s[i] == "(":
                cout += 1

            else: 
                cout -= 1 

            if cout == 0:
                res += s[start + 1:end]
                start = end + 1
            
        return res

            

    