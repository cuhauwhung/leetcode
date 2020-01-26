#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        def dfs(grid, x, y, n, m):

            if x < 0 or y < 0 or x >= n or y >= m or grid[y][x] == '0':
                return

            grid[y][x] = '0'
            dfs(grid, x + 1, y, n, m)
            dfs(grid, x - 1, y, n, m)
            dfs(grid, x, y + 1, n, m)
            dfs(grid, x, y - 1, n, m)

        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])

        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    ans += 1
                    dfs(grid, x, y, n, m)
        return ans

# @lc code=end