class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        pairs = set(zip(s, t))  
        unique_s = set(s)        
        unique_t = set(t)        

        if len(pairs) == len(unique_s) == len(unique_t):
            return True
        else:
            return False
        