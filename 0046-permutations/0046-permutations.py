class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [-1] * (len(nums) + 1)
        used = [False] * (len(nums) + 1)
        k = []

        def Try(t):
            for i in range(0,len(nums)):
                if not used[i] and ans[t] == -1:
                    ans[t] = nums[i]
                    used[i] = True
                    if t == len(nums):
                        k.append(ans[1:])
                    else:
                        Try(t+1)
                    ans[t] = -1
                    used[i] = False

        Try(1)    
        return k