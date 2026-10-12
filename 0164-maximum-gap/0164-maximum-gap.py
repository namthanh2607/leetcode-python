class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        if len(nums) <= 1:
            return 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > res:
                res = nums[i] - nums[i-1]
        return res