#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # key: use DP
        #      dp[i][j] = length of square at original matrix 
        #                  - if matrix[i][j] = 0 -> dp[i][j] would be 0 
        #                  - if dp[i-1][j], dp[i][j-1], and dp[i-1][j-1] 
        #                    are all 1s, and matrix[i][j] == 1 
        #                    then only will be able to += 1 

        if not matrix: return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(c)] for i in range(r)]
        res = max(max(dp))

        for i in range(1, r):
            for j in range(1, c):

                # if matrix[i][j] == 0, then we should just ignore
                dp[i][j] = (min(dp[i-1][j-1], 
                            dp[i][j-1], 
                            dp[i-1][j]) + 1 ) * int(matrix[i][j])
                            
                res = max(res, dp[i][j]**2)
        return res

# @lc code=end