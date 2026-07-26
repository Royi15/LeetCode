class Solution(object):
    def isHappy(self, n):
        if n == 1:
            return True
        s = set()
        total = sum(int(digit)**2 for digit in str(n))
        while total != 1:
            total = sum(int(digit)**2 for digit in str(total))
            if total in s:
                return False
            s.add(total)

        return True

        