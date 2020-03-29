
#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#

# @lc code=start

class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        # key: use DP 
        #      num_ways_diff[i] = num_ways[i-1] * (k-1)
        #      num_ways_same[i] = num_ways_diff[i-1] * 1                        
        #       -- num_ways_diff[i-1] <- all the cases where the i-1th and i-2th are different.
        #
        #      num_ways[i] = num_ways_diff[i] + num_ways_same[i]
        #                  = num_ways[i-1] * (k-1) + num_ways_diff[i-1]
        #                  = num_ways[i-1] * (k-1) + num_ways[i-2] * (k-1) 
        
        if n == 0: return 0
        if n == 1: return k
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = k
        dp[2] = k*k
                
        for i in range(3, n+1):
            dp[i] = (dp[i-2] + dp[i-1]) * (k-1) 
            
        return dp[-1]

# @lc code=end
