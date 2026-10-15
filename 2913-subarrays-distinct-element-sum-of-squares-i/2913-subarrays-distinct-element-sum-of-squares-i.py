class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ret = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                ret.append(len(set(nums[i:j + 1])))
        return sum(x**2 for x in ret)
        