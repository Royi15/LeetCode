class Solution(object):
    def containsDuplicate(self, nums):
       new_arr = list(set(nums))

       return len(new_arr) != len(nums)
        