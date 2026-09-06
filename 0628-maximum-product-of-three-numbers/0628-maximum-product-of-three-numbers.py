class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[1] <= 0:
            return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])
        else:
            return nums[-3] * nums[-2] * nums[-1]
        