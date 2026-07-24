class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {num: i for i, num in enumerate(nums)}

        for i in range(len(nums)):
            if (target - nums[i]) in d:
                if i != d[target - nums[i]]:
                    return [i, d[target - nums[i]]]

        return []



        