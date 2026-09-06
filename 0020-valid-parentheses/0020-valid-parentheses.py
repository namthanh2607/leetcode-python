class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "(": ")",
            '[': ']',
            '{': '}'
        }
        for i in s:
            if len(stack) == 0 and i not in mapping:
                return False
                break
            if len(stack) == 0 or i in mapping:
                stack.append(i)
            else:
                if i == mapping.get(stack[-1]):
                    stack.pop(-1)
                else: 
                    return False
                    break
        if len(stack) == 0:
            return True
        else:
            return False


      

        