class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse = True)
        targets =[target]
        sav = []
        ans = []
        def solution():
            ans.append(sav[:])
        def Try(t): # t la index ptu trong cand, i la 
            if t == len(candidates) or targets[0] < 0:
                return
            for i in range(targets[0]//candidates[t]+1):
                targets[0] = targets[0] - i * candidates[t]
                for j in range(i):
                    sav.append(candidates[t])
                if targets[0] == 0:
                    solution()
                else:
                    Try(t+1)
                for j in range(i):
                    sav.pop()
                targets[0] = targets[0] + i * candidates[t]

        Try(0)
        return ans
