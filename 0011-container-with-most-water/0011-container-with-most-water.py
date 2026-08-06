class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        s_max = 0
        while left < right:
            s = (right - left)*min(height[left],height[right])
            s_max = max(s,s_max)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return s_max      