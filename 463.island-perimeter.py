#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        num = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r == 0 or grid[r-1][c] == 0:
                        num += 1
                    if r == m-1 or grid[r+1][c] == 0:
                        num += 1
                    if c == 0 or grid[r][c-1] == 0:
                        num += 1
                    if c == n-1 or grid[r][c+1] == 0:
                        num += 1
        return num 
# @lc code=end

