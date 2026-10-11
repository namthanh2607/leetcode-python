class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = sum([nums[x - 1]**2 for x in range(1,len(nums) + 1) if n % x == 0])
        return res        