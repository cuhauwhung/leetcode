#
# @lc app=leetcode id=490 lang=python3
#
# [490] The Maze
#

# @lc code=start
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        queue = [start]
        n = len(maze)
        m = len(maze[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        while queue:
            i, j = queue.pop(0)
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True
            
            for x, y in dirs:

                row = i + x
                col = j + y

                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y

                row -= x
                col -= y
                
                if maze[row][col] == 0:
                    queue.append([row, col])
        
        return False

# @lc code=end

