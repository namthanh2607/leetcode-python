class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] % k == 0 and nums[i] not in ans:
                ans.append(nums[i])
        if not ans or ans[0] != k:
            return k
        for i in range(len(ans)):
            if ans[i] != (i + 1) * k:
                return (i + 1) * k
        return (len(ans) + 1) * k
            
                