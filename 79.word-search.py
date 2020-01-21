#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start

class Solution:
    def exist(self, board, word):
        visited = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, visited):
                    return True
        
        return False

    def dfs(self, board, word, i, j, visited, pos = 0):

        if pos == len(word):
            return True

        if (i < 0 or i >= len(board) 
            or j < 0 or j >= len(board[0]) 
            or visited.get((i, j)) 
            or word[pos] != board[i][j]):
            return False

        visited[(i, j)] = True
        res = self.dfs(board, word, i, j + 1, visited, pos + 1) \
                or self.dfs(board, word, i, j - 1, visited, pos + 1) \
                or self.dfs(board, word, i + 1, j, visited, pos + 1) \
                or self.dfs(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False

        return res

# @lc code=end
