class Solution:
    def generateParenthesis(self, n: int):


        M = [""] * (n*2+1)
        back = [""] * (n*2+1)
        K = []
        count = [0]

        def solution():
            t = "".join(M)
            if t not in K:
                K.append(t)

        def Try(t):
            for i in ["(",")"]: 
                if back[t] == "" and count[0] > 0:
                    M[t] = i
                    back[t] = 1

                    if M[t] == "(":
                        count[0] = count[0] + 1
                    else:
                        count[0] = count[0] - 1
                    
                elif back[t] == "" and count[0] == 0:
                    M[t] = "("
                    count[0] = count[0] + 1
                    back[t] = 1

                if count[0] == 0 and t == 2*n:
                    solution()
                elif t == 2*n:
                    None
                else: 
                    Try(t+1)

                #  dkien back
                if M[t] == "(":
                    count[0] = count[0] - 1
                else:
                    count[0] = count[0] + 1
                back[t] = ""
        Try(1)
        return K




