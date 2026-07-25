class Solution(object):
    def myAtoi(self, s):
        sum = 0
        carry = 1
        arr = []
        s = s.lstrip()
        if not s:
            return 0
        flag = 0
        if s[0] == "-":
            flag = 1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        for c in s:
            try:
                arr.append(int(c))
            except ValueError:
                break

        for digit in arr:
            sum = sum * 10 + digit

        num = sum if flag == 0 else -1 * sum
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num

        


        