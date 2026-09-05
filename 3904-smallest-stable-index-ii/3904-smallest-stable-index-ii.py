class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        list_max = [nums[0]]
        list_min = [nums[-1]]
        for i in range(1,len(nums)):
            list_max.append(max(list_max[-1],nums[i]))
            list_min.append(min(list_min[-1],nums[-1 - i]))
        for i in range(len(nums)):
            if list_max[i] - list_min[len(nums) - i - 1] <= k:
                return i
        return -1
