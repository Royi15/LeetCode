import heapq 
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        heap = []
        result= []

        for v,c in freq.items():
            heapq.heappush(heap,(-c,v))

        for i in range(k):
            pair = heapq.heappop(heap)
            result.append(pair[1])

        return result

        


        