class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = n - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total == 0:
                    ans.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1

                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1

                elif total < 0:
                    start += 1 

                else:
                    end -= 1  

        return ans 





        