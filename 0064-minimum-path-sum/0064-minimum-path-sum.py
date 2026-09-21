class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for j in range(0,n-1):
            grid[0][j + 1] += grid[0][j] 
        for i in range(0,m-1):
            grid[i + 1][0] += grid[i][0]        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) 
        return grid[m-1][n-1]
        