class Solution(object):
    def partitionLabels(self, s):
        last = {}
        result = []

        for i, c in enumerate(s):
            last[c] = i

        temp = []
        end = 0

        for i in range(len(s)):
            temp.append(s[i])
            end = max(end, last[s[i]])

            if i == end:
                result.append(temp)
                temp = []

        return [len(x) for x in result]



            



