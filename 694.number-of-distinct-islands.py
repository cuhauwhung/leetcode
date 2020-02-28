#
# @lc app=leetcode id=694 lang=python3
#
# [200] Number of Distinct Islands
#

# @lc code=start

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        distinct_islands = set()
        ans = 0 
        
        def dfs(grid, i, j, i_0, j_0, m, n, curr):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0 
                curr.add((i - i_0, j - j_0))
                dfs(grid, i-1, j, i_0, j_0, m, n, curr)
                dfs(grid, i+1, j, i_0, j_0, m, n, curr)
                dfs(grid, i, j-1, i_0, j_0, m, n, curr)
                dfs(grid, i, j+1, i_0, j_0, m, n, curr)
            return curr 
                      
        m = len(grid)
        n = len(grid[0])
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    vals = dfs(grid, i, j, i, j, m, n, set())

                    if vals not in distinct_islands:
                        distinct_islands.add(frozenset(vals))
                        ans += 1
                        
        return ans
# @lc code=end