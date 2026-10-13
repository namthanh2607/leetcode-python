class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        new_score = [abs(x) for x in nums]
        new_score.sort(reverse = True)
        print(new_score)
        res = 0
        for i in range((len(nums) - 1) // 2 + 1):
            res += new_score[i]**2 
        for i in range((len(nums) - 1) // 2 + 1, len(nums)):
            res -= new_score[i]**2
        return res
        