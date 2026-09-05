class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_cur = nums[0]
        for i in range(len(nums)):
            max_cur = max(max_cur,nums[i])
            if max_cur - min(nums[i:len(nums)]) <= k:
                return i
        return -1
