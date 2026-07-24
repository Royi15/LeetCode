class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])  
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = result[-1]
            curr = intervals[i]

            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])  
            else:
                result.append(curr)

        return result
        