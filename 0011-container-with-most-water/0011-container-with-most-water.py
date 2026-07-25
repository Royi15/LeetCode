class Solution(object):
    def maxArea(self, height):
        left = 0 
        right = len(height) - 1
        max = 0

        while left < right:
            sum = min(height[right], height[left]) * (right - left)
            if sum > max:
                max = sum
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return max
        