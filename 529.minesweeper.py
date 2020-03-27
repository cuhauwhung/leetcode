#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        if not board: return []
        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        def dfs(board, x, y):
            
            if board[x][y] != "E": return 
            moves = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, 1), (-1, -1), (1,-1)]
            mine_count = 0 
            
            for dx, dy in moves:
                newx, newy = x + dx, y + dy 
                if 0 <= newx < m and 0 <= newy < n and board[newx][newy] == "M": 
                    mine_count += 1 
                
            if mine_count == 0:
                board[x][y] = "B"

            else:
                board[x][y] = str(mine_count)
                return 

            for dx, dy in moves:
                newx, newy = x + dx, y + dy 
                if 0 <= newx < m and 0 <= newy < n: 
                    dfs(board, newx, newy)

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        dfs(board, i, j)
        return board 

# @lc code=end