class Solution(object):
    def reverseBits(self, n):
        b = bin(n)[2:].zfill(32)
        rev = b[::-1]
        n = int(rev,2)
        
        return n