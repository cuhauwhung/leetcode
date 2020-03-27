#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        moves = [(0, 1), (1,0), (-1,0), (0, -1)]
        n, m = len(image), len(image[0])
        def dfs(sr ,sc, visited):
            visited.add((sr, sc))
            for dx, dy in moves: 
                newx, newy = sr + dx, sc + dy
                if 0 <= newx < n and 0 <= newy < m and (newx, newy) not in visited and image[newx][newy] == image[sr][sc]:
                    dfs(newx, newy, visited)
            image[sr][sc] = newColor

        visited = set()
        dfs(sr, sc, visited)
        return image 
# @lc code=end

