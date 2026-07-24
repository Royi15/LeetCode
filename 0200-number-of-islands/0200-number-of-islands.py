class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        col = len(grid[0])
        count = 0
        
        def dfs(grid,r,c):
            if (r >= rows or r < 0 or c >= col or c < 0):
                return 
            
            if (grid[r][c] != "1"):
                return 

            grid[r][c] = "0"

            dfs(grid, r +1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c -1)

        for i in range(rows):
            for j in range(col):
                if(grid[i][j] == "1"):
                    dfs(grid,i,j)
                    count = count+1

        return count

            
        