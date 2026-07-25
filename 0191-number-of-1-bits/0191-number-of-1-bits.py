class Solution(object):
    def hammingWeight(self, n):
        count = 0
        b = bin(n)[2:]
        for i in range(len(b)):
            if (int(b[i]) == 1):
                count = count + 1

        return count
        