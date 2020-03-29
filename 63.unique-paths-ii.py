#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # key: use DP
        #      dp[i][j] = # of unique paths to (i, j)

        if not obstacleGrid: return 

        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        
        for i in range(1, r):
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])

        for i in range(1, c):
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])

        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])

        return dp[-1][-1]



# @lc code=end

