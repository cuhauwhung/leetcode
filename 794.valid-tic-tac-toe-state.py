#
# @lc app=leetcode id=794 lang=python3
#
# [794] Valid Tic-Tac-Toe State
#

# @lc code=start
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
                
        def isWin(board, c):
            for i in range(3):  # Row check
                if board[i] == c*3:
                    return True
                
            for i in range(3):  # Column check
                if board[0][i] == c and board[1][i] == c and board[2][i] == c:
                    return True
                
            if (board[0][0] == c and board[1][1] == c and board[2][2] == c) or \
                (board[0][2] == c and board[1][1] == c and board[2][0] == c):  # Diagonal check
                return True
            
            return False

        count_X = count_O = 0
        
        for i in range(3):
            for j in range(3):
                count_X += 1 if board[i][j] == 'X' else 0
                count_O += 1 if board[i][j] == 'O' else 0
                
        if count_O > count_X or count_X > count_O + 1:
            return False
        
        if count_O == count_X and isWin(board, 'X') or count_X == count_O + 1 and isWin(board, 'O'):
            return False
        
        return True 
# @lc code=end

