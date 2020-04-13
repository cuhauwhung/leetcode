
#
# @lc app=leetcode id=256 lang=python3
#
# [256]  Paint House
#

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        # key: use DP, have to make decisions at each house
        
        if not costs: return 0
        r, c = len(costs), len(costs[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0] = costs[0]
        
        for i in range(1, r):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
        return min(dp[-1])
