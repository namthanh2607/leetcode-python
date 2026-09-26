class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        self.ans = []
        self.ret = []
        self.Try(0, 4, len(s), s)
        return self.ret

    def Solution(self):
        self.ret.append(".".join(self.ans))

    def Try(self, k, goal, leng, s):
        if goal == 0 and leng == 0:
            self.Solution()
            return
            
        elif goal == 0:
            return

        for i in range(1, 4):
            if i > leng:
                break

            if s[k] == '0':
                self.ans.append('0')
                self.Try(k + 1, goal - 1, leng - 1, s)
                self.ans.pop()
                break  

            elif 0 <= int(s[k : k + i]) <= 255:
                self.ans.append(s[k : k + i])
                self.Try(k + i, goal - 1, leng - i, s)
                self.ans.pop()