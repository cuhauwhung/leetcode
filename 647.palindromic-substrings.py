#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # key: use DP 
        #      dp[i][j] = if string is palindrome at the indexes

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for start in range(n-1, -1, -1):
            for end in range(start + 1, n):
                dp[start][end] = 1 if (s[start] == s[end] and 
                                        (dp[start+1][end-1] or end == start + 1)) else 0 
        
        print(dp)
        count = 0
        for this_row in dp:
            count += sum(this_row)
            
        return count  
# @lc code=end

