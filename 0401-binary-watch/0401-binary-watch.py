class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        if turnedOn == 0:
            return ["0:00"]
        self.turnedOn = turnedOn
        self.M = [0] * 10
        self.ret = []
        self.backtrack(0,0,self.M)
        self.change(self.ret)
        return self.ans

    def solution(self,M):
        self.ret.append(M[:])

    def backtrack(self,t,count,M):
        if count > self.turnedOn or t >= 10:
            return

        for i in range(t,10):
            M[i] = 1
            if count + 1 == self.turnedOn:
                self.solution(M) 
            self.backtrack(i + 1,count + 1,M)
            M[i] = 0

    def change(self, ret):
        self.ans = []
        for i in ret:
            if i[0] + 2*i[1] + 4*i[2] + 8*i[3] <= 11 and 1*i[4] + 2*i[5] + 4*i[6] + 8*i[7] + 16*i[8] + 32*i[9] <= 59 :
                if 1*i[4] + 2*i[5] + 4*i[6] + 8*i[7] + 16*i[8] + 32*i[9] >= 10:
                    self.ans.append(str(i[0] + 2*i[1] + 4*i[2] + 8*i[3]) + ":" + str(1*i[4] + 2*i[5] + 4*i[6] + 8*i[7] + 16*i[8] + 32*i[9]))
                else:
                    self.ans.append(str(i[0] + 2*i[1] + 4*i[2] + 8*i[3]) + ":0" + str(1*i[4] + 2*i[5] + 4*i[6] + 8*i[7] + 16*i[8] + 32*i[9]))
        return self.ans
                
            


        