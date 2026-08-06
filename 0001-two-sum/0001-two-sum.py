class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind1 in range(len(nums)-1):
            need = target - nums[ind1]
            for ind2 in range(ind1 + 1,len(nums)):
                if nums[ind2] == need:
                    return [ind1,ind2]
          


        