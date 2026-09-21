class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                count += 1
                if count > 1:
                    nums.pop(i)
                else:
                    i += 1
            else:
                count = 0
                i += 1
        return len(nums)
