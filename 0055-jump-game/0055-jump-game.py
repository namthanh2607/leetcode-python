class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0
        if len(nums) == 1:
            return True
        else:
            for i in range(len(nums)):
                if i <= max_ind:
                    max_ind = max(max_ind , i + nums[i])
                    if max_ind + 1 >= len(nums):
                        return True
                else:
                    return False
            
