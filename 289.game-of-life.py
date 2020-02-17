#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        rows = len(board)
        cols = len(board[0])
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        for i in range(rows):
            for j in range(cols):
                live_neighbors = 0 
                for neighbor in neighbors: 
                    r = i + neighbor[0]
                    c = j + neighbor[1]

                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1
                
                if copy_board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 0

                if copy_board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 1
                    
 # @lc code=end
                    