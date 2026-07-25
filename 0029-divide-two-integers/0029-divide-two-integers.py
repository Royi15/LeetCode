class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  

        a, b = abs(dividend), abs(divisor)
        result = 0

        while a >= b:
            temp, multiple = b, 1
       
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple

   
        if (dividend < 0) != (divisor < 0):
            result = -result

        return result



        