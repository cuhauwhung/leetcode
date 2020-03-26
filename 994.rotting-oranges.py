#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque 

        # key: find all rotten then perform bfs on each 
        n = len(grid)
        m = len(grid[0])
        moves = [(1,0), (0,1), (-1,0), (0,-1)]

        lvl = 0
        queue = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, lvl))
                    grid[i][j] = 0
        
        while queue:
            curx, cury, lvl = queue.popleft()
            for dx, dy in moves:
                newx, newy = curx + dx, cury + dy
                if 0 <= newx < n and 0 <= newy < m and grid[newx][newy] == 1:
                    queue.append((newx, newy, lvl + 1))
                    grid[newx][newy] = 0
                    
        if any(1 in row for row in grid):
            return -1
        
        return lvl
# @lc code=end

