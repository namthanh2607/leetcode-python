class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        change = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        res = 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ['+','-','*','/']:
                y, x = int(stack.pop()), int(stack.pop())
                stack.append(int(change[tokens[i]](x, y)))
            else:
                stack.append(int(tokens[i]))

        return stack[-1]


        