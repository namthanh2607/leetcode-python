class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        targets = [target]
        candidates.sort()
        M = []
        ans = []

        def Try(t): # t la index 
            if targets[0] < 0 or t >= len(candidates):
                return False
            for i in range(t , len(candidates)):
                if i > t and candidates[i] == candidates[i - 1]:
                    continue
                targets[0] -= candidates[i]
                M.append(candidates[i])
                if targets[0] == 0:
                    ans.append(M[:])
                Try(i + 1)
                targets[0] += candidates[i]
                M.pop()

        Try(0)
        return ans        