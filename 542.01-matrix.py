#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import deque
        
        n = len(matrix)
        m = len(matrix[0])
        moves = [(0, 1), (0, -1), (-1, 0), (1,0)]
        
        def bfs(i, j, matrix):
            queue = deque([(i, j, 0)])
            visited = {(i , j)}
            
            while queue:
                x, y, level = queue.popleft()
                if matrix[x][y] == 0:
                    return level
                
                for dx, dy in moves:
                    newx, newy = x + dx, y + dy
                    if 0 <= newx < n and 0 <= newy < m and (newx, newy) not in visited:
                        queue.append((newx, newy, level+1))
                        visited.add((newx, newy))

        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1: 
                    ans[i][j] = bfs(i, j, matrix) 
        return ans        
# @lc code=end

