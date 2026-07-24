class Solution(object):
    def threeSum(self, nums):
        res = set()
        nums.sort()
        n = len(nums)

        for i in range(n-2):

            j = i+1
            k= n-1

            while j<k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j=j+1

                elif total > 0:
                    k=k-1

                else:
                    res.add((nums[i],nums[j],nums[k]))
                    j=j+1

        res = [list(triplet) for triplet in res]
        return res

        
            

        
        