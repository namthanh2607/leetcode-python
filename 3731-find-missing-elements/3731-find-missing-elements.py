class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums) - 1:
            if nums[i] + 1 != nums[i+1]:
                ans.append(nums[i] + 1)
                nums[i] += 1
            else:
                i += 1
        return ans    
        