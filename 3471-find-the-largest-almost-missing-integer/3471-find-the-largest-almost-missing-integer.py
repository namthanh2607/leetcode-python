class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        elif k == len(nums):
            return max(nums)
        elif k == 1:
            nums.sort(reverse = True)
            for i in nums:
                if nums.count(i) == 1:
                    return i
            return -1
        elif nums[0] == nums[-1]:
            return -1
        else:
            if nums.count(nums[-1]) == 1 and nums.count(nums[0]) == 1:
                return max(nums[-1],nums[0])
            elif nums.count(nums[-1]) != 1 and nums.count(nums[0]) == 1:
                return nums[0]
            elif nums.count(nums[-1]) == 1 and nums.count(nums[0]) != 1:
                return nums[-1]
            return -1
            
        