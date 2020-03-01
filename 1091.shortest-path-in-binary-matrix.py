#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        visited = set((0, 0))
        queue = deque([(0, 0, 1)])
        n, m = len(grid), len(grid[0])

        while queue:
            x, y, lvl = queue.popleft()
            if (x, y) == (n-1, m-1): return lvl

            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, lvl + 1))

        return -1 





# @lc code=end

