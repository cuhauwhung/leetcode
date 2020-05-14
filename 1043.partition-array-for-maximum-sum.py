#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:

        # key: use DP 
        #      dp[i] := max sum of A[1] ~ A[i]

        N = len(A)
        dp = [0] * (N + 1)
        for i in range(N):
            curMax = 0
            for k in range(min(K, i + 1)):
                curMax = max(curMax, A[i - k])
                dp[i] = max(dp[i], dp[i - 1 - k] + curMax * (k + 1))
        return dp[N - 1]

# @lc code=end

