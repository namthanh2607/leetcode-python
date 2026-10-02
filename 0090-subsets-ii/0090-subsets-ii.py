class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        def Try(t,cur):
            if t >= len(nums):
                res.append(cur[::])
                return
            
            cur.append(nums[t])
            Try(t + 1, cur)
            cur.pop()

            # ko chon 2 -> bo het con 2 dang sau 
            while t < len(nums) - 1 and nums[t] == nums[t+1]:
                t += 1

            Try(t + 1, cur)
            

        Try(0,[])
        return res

        