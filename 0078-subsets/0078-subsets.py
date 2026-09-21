class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        M = [] 
        ans = [[]] # Start with the empty subset

        def Try(start):
            for i in range(start, len(nums)):
                M.append(nums[i])
                ans.append(M.copy()) # Record the subset
                
                Try(i + 1) # Move to the next index
                
                M.pop() # Backtrack

        Try(0) # Start from index 0
        return ans





        