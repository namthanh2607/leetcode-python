class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_val = max(nums)
        min_val = min(nums)
        ind_min = nums.index(min_val)
        ind_max = nums.index(max_val)
        return min(max(ind_min + 1, ind_max + 1) ,min(ind_min,ind_max) + 1 + len(nums) - max(ind_min,ind_max), max(len(nums) - ind_min, len(nums) - ind_max))
        