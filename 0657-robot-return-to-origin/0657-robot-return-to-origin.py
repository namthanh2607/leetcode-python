class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count_u,count_d,count_l,count_r = 0,0,0,0
        for i in moves:
            if i == "L":
                count_l += 1
            elif i == "R":
                count_r += 1
            elif i == "U":
                count_u += 1
            else:
                count_d += 1    
        return (count_l == count_r) and (count_u == count_d)


        