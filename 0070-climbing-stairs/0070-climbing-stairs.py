class Solution(object):
    def climbStairs(self, n):
        if(n == 1):
            return 1

        if(n == 2):
            return 2
        a1 = 1
        a2 = 2
       

        for i in range (n-2):
            next_val = a1 + a2
            a1 = a2
            a2 = next_val
            n -= 1

        return next_val


    

        
        