#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix: return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(c)] for i in range(r)]
        res = max(max(dp))

        for i in range(1, r):
            for j in range(1, c):

                # if matrix[i][j] == 0, then we should just ignore
                dp[i][j] = (min(dp[i-1][j-1], 
                            dp[i][j-1], 
                            dp[i-1][j])+1) * int(matrix[i][j])
                            
                res = max(res, dp[i][j]**2)
        return res

# @lc code=end