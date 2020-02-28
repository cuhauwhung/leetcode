#
# @lc app=leetcode id=723 lang=python3
#
# [723] Candy Crush
#

# @lc code=start


class Solution:
    def candyCrush(self, M: List[List[int]]) -> List[List[int]]:
        while True:
            # 1, Check
            crush = set()
            for i in range(len(M)):
                for j in range(len(M[0])):
                    if j > 1 and M[i][j] and M[i][j] == M[i][j - 1] == M[i][j - 2]:
                        crush = crush | {(i, j), (i, j - 1), (i, j - 2)}

                    if i > 1 and M[i][j] and M[i][j] == M[i - 1][j] == M[i - 2][j]:
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}

            # 2, convert indexes in crush to 0
            if not crush: break
            for i, j in crush: 
                M[i][j] = 0
            
            # 3, move values to appropriate indexes
            for j in range(len(M[0])):
                idx = len(M) - 1
                for i in reversed(range(len(M))):
                    if M[i][j]:
                        M[idx][j] = M[i][j]
                        idx -= 1
                        
                for i in range(idx + 1): 
                    M[i][j] = 0
        return M

