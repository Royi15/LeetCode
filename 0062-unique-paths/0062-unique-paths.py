class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j]= matrix[i-1][j] + matrix[i][j-1]

        return matrix[n-1][m-1]
