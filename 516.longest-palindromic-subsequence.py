#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # key: use DP 
        #      dp[i][j] = longest subsequence that is paindrome at indexes

        if s == s[::-1]: return len(s)
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        for start in range(n - 1, -1, -1):
            dp[start][start] = 1 
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    dp[start][end] = 2 + dp[start+1][end-1]
                else:
                    dp[start][end] = max(dp[start+1][end], dp[start][end-1])
        
        return dp[0][n-1]
# @lc code=end

