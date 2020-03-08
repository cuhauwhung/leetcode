#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#

# @lc code=start
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def dfs(x, y, seen):
            temp = []
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] and (nx,ny) not in seen:
                    seen.add((x, y))
                    temp = temp + [dfs(nx, ny, seen)]
                    seen.remove((x,y))
            return (max(temp) if temp else 0) + grid[x][y]
            
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    temp = dfs(i, j, {(i,j)})
                    ans = max(ans, temp)
        return ans
# @lc code=end

