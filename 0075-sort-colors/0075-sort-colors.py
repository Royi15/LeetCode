class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = 0
        blue = len(nums) - 1
        mid= 0 

        while mid <= blue:
            if nums[mid] == 0: #red
                nums[red],nums[mid] = nums[mid], nums[red]
                red = red +1
                mid = mid + 1

            elif nums[mid] == 1: #white
                mid = mid +1
            
            else:
                nums[blue],nums[mid] = nums[mid], nums[blue]
                blue = blue -1
                