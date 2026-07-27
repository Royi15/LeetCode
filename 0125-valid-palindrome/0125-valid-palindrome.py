class Solution(object):
    def isPalindrome(self, s):
        filtered = [ch.lower() for ch in s if ch.isalnum()]  
        return filtered == filtered[::-1]
        