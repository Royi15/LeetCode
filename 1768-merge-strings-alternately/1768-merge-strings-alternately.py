class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        flag = 0 
        newWord= ""

        for i in range(len(word1) + len(word2)):
            if flag == 0 and word1:
                newWord += word1[0]
                word1 = word1[1:]
            elif word2:
                newWord += word2[0]
                word2 = word2[1:]
            flag = 1-flag

        if word1:
            newWord += word1
        elif word2:
            newWord += word2

        return newWord

            



