class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M = [nums[0]] + [-1e9] * (len(nums) - 1)
        def F(n):
            if n != 0:
                M[n] = max(nums[n],F(n-1) + nums[n])
            return M[n]
        F(len(nums) - 1)
        return max(M)