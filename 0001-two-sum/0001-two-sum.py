class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visit = {} 
        for i, num in enumerate(nums):
            need = target - num
            if need in visit:
                return [visit[need], i]
            visit[num] = i
        