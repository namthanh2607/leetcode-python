class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        Try = 1
        start = 0
        while start < len(nums):
            if nums[start] < Try * k:
                start += 1
            elif nums[start] == Try * k:
                Try += 1
            elif nums[start] > Try * k:
                return Try * k 
        return Try * k
            
                