class Solution(object):
    def merge(self, nums1, m, nums2, n):
         
        nums1[:] = nums1[:m]
    
        i = 0 
        while i < n:
            inserted = False
            for j in range(len(nums1)):
                if nums2[i] <= nums1[j]:
                    nums1.insert(j, nums2[i])
                    inserted = True
                    break
            if not inserted:
                nums1.append(nums2[i])
            i += 1
        

        
        