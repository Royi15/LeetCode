class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)        
        cols = len(obstacleGrid[0])
        matrix = [[0] * cols  for _ in range(rows)]

        if obstacleGrid[0][0] == 1:
            return 0
        else:
            matrix[0][0] =1

        for i in range(1,rows):
            if obstacleGrid[i][0] == 1:
                matrix[i][0] = 0
            else:
                matrix[i][0] = matrix[i-1][0]

        for j in range(1,cols):
            if obstacleGrid[0][j] == 1:
                matrix[0][j] = 0
            else:
                matrix[0][j] = matrix[0][j-1]

        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[rows-1][cols-1] 

                
                


        