class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix)

        while left != right and left != right - 1:
            mid = (left + right)//2
            if matrix[mid][0] > target:
                right = mid
            elif matrix[mid][0] < target:
                left = mid
            else:
                return True
        x = left

        left = 0
        right = len(matrix[0])

        while left != right and left != right - 1:
            mid = (left + right)//2
            if matrix[x][mid] > target:
                right = mid
            elif matrix[x][mid] < target:
                left = mid
            else:
                return True

        return matrix[x][left] == target