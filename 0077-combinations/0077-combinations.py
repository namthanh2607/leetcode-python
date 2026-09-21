class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        M = [0] * (k + 1)
        ans = []
        def Try(t):
            for i in range(M[t-1] + 1, n - k + t + 1):
                M[t] = i
                if t == k:
                    ans.append(M[1:])
                else:
                    Try(t+1)
        Try(1)
        return ans




