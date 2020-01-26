#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        def dfs(grid, i, j, n, m):

            if (i < 0 or j < 0 or 
                i >= len(grid) or j >= len(grid[0]) 
                or grid[i][j] == 0):
                return 0

            grid[i][j] = 0 
            return (1 + dfs(grid, i+1, j, n, m) + 
                    dfs(grid, i-1, j, n, m) + 
                    dfs(grid, i, j+1, n, m) + 
                    dfs(grid, i, j-1, n, m))

        max_area = 0 
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    max_area = max(dfs(grid, i, j, n,m ), max_area)

        return max_area 
# @lc code=end

