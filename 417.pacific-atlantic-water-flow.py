#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        def dfs(matrix, i, j, visited, m, n):
            visited[i][j] = True
            for dx, dy in moves:
                newX, newY = i + dx, j + dy
                if newX < 0 or newX >= m or newY < 0 or newY >= n or visited[newX][newY] or matrix[newX][newY] < matrix[i][j]:
                    continue
                dfs(matrix, newX, newY, visited, m, n)

        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        moves = [(1,0),(-1,0),(0,1),(0,-1)]

        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []

        # try to go from the ocean back to the land
        for i in range(m):
            dfs(matrix, i, 0, p_visited, m, n)
            dfs(matrix, i, n-1, a_visited, m, n)
            
        for j in range(n):
            dfs(matrix, 0, j, p_visited, m, n)
            dfs(matrix, m-1, j, a_visited, m, n)
            
        # if a spot is visited by both oceans, then add to final results
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i,j])
        return result
                
        
# @lc code=end

