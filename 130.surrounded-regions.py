#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # key: we have to start DFS from the borders (north, south, east, west) and turn all the explored paths from the borders into N. Then go through all nodes and turn N -> O and O -> X

        def dfs(board, i, j, R, C):
            if 0<=i<R and 0<=j<C and board[i][j] == "O":
                board[i][j] = "N"
                dfs(board, i, j+1, R, C)
                dfs(board, i, j-1, R, C)            
                dfs(board, i-1, j, R, C)            
                dfs(board, i+1, j, R, C)   

        if not board or not board[0]: return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2: return
        
        # start from the border and replace all O to N
        # put all the border value into queue.
        for i in range(R):
            dfs(board, i, 0, R, C) 
            dfs(board, i, C-1, R, C)

        for j in range(C):
            dfs(board, 0, j, R, C)
            dfs(board, R-1, j, R, C)

        # replace all the O to X, then replace all the N to O
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "N":
                    board[i][j] = "O"
        
                    



# @lc code=end

