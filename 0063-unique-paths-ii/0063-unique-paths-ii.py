class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ban = []
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    ban.append([i,j])
        if [m-1,n-1] in ban or [0,0] in ban:
            return 0                    
        obstacleGrid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if [i,j] not in ban:
                    if i < m - 1:
                        obstacleGrid[i + 1][j] += obstacleGrid[i][j]
                    if j < n - 1:
                        obstacleGrid[i][j + 1] += obstacleGrid[i][j]
        return obstacleGrid[m-1][n-1]