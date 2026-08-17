class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 1e9
        if nums[0] >= target and nums[0] > 0:
            return nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            start = i + 1
            end = n - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]

                if total == target:
                    return total
                    
                else:
                    if abs(ans - target) > abs(total - target):
                        ans = total
                    
                    if total - target > 0:
                        end -= 1
                    else:
                        start += 1
        return ans



