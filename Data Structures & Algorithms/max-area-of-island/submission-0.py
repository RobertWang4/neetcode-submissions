class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if(
                r < 0 or r >= len(grid) or 
                c < 0 or c >= len(grid[0]) or 
                grid[r][c] ==0):
                return 0

            count = 1
            grid[r][c] = 0

            count += dfs(r-1,c)
            count += dfs(r+1,c)
            count += dfs(r,c-1)
            count += dfs(r,c+1)
            return count

        maxLand = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxLand = max(maxLand,dfs(i,j))
        return maxLand