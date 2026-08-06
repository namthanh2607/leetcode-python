class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = [0,0,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        M = [""] * (len(digits) + 1)
        used = [0]*(len(digits) + 1)
        K = []

        def solution():
            K.append("".join(M))


        def Try(t):
            for i in nums[int(digits[t-1])]:
                if used[t] == 0 and t > 0:
                    M[t] = str(i)
                    used[t] = 1
                    if t == len(digits):
                        solution()
                    else:
                        Try(t+1)
                    used[t] = 0
        Try(1)
        return K
                