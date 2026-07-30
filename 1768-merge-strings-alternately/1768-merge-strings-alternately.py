class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newWord = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            newWord.append(word1[i])
            newWord.append(word2[j])
            i += 1
            j += 1

        newWord.append(word1[i:])
        newWord.append(word2[j:])
        
        return "".join(newWord)
            



