#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: 
            return s 

        dp = [[0 for j in range(n)] for i in range(n)]
 
        # fill diagonals with 1 
        for i in range(n):
            dp[i][i] = 1
            ans = s[i]

        maxLen = 1
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):    

                dp[start][end] = 1 if (s[start] == s[end] and (dp[start+1][end-1] or end == start + 1)) else 0 

                if dp[start][end] == 1 and maxLen < end - start + 1:
                    maxLen = end - start + 1
                    ans = s[start: end+ 1]

        return ans 






# @lc code=end

