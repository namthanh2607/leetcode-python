class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            check = 0
            for j in str(nums[i]):
                check += int(j)
            if check == i:
                return i
                
        return -1
        