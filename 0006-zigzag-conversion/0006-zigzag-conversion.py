class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        rows = []

        for i in range(numRows):
            rows.append([])
        
        flag =0
        counter = 0

        for i in range(len(s)):
            rows[counter].append(s[i])

            if counter == numRows -1:
                flag = 1
            
            if counter == 0:
                flag = 0


            if flag == 0:
                counter += 1
            else:
                counter -= 1
            
            
        result = ""

        for row in rows:
            for char in row:
                result = result + char

        return result

        



        