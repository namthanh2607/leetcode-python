class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        def Try(t,cur):
            if t == len(nums):
                if cur not in res:
                    res.append(cur[::])
                return
            
            Try(t + 1, cur)

            cur.append(nums[t])
            Try(t + 1, cur)
            cur.pop()

        Try(0,[])
        return res

        