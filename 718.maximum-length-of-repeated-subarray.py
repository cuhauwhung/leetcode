#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:

        # key: use DP 
        #      dp[i][j] = length of max repeated subarray
        #                  at A[:i] and B[:j]
        
        n, m = len(A), len(B)
        max_val = 0
        dp=[[0]*(m + 1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1 
                    max_val = max(max_val, dp[i][j])
        return max_val
# @lc code=end

