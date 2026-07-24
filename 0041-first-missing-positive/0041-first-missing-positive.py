class Solution(object):
    def swap(self,nums,i,j):
            nums[i],nums[j] = nums[j], nums[i]

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n= len(nums)

        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i]-1]:
                self.swap(nums, i, nums[i] -1 )

        for i in range(n):
            if nums[i] != i + 1:
                return i+1

        return n+1 