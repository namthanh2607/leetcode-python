class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        for i in range(0,len(nums)):
            if i == 0:
                if len(nums) >= 2 and nums[0] <= nums[1]:
                    continue
                else:
                    return 0
            elif 0 < i < len(nums) - 1:
                if nums[i-1] < nums[i] and nums[i] > nums[i + 1]:
                    return i
            else:
                if nums[-1] > nums[-2]:
                    return len(nums) - 1


        