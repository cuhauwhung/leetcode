#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # key: use DP 
        #      dp[i][j] = profit if we performed rest, buy, sell on day i 

        if not prices: return 0 
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]

        # max profit we get on day n if we: rest, buy, sell 
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = float('-inf')
        bought = dp[0][1]
         
        n = len(prices)
        for i in range(1, n):

            # if we rest on day n, don't care what we did n-1; just take max 
            dp[i][0] = max([dp[i-1][0], dp[i-1][2], dp[i-1][1]])

            # if we buy on day n, cannot buy on day n-1 and also cannot sell on n-1. 
            # All we can do is rest 
            dp[i][1] = dp[i-1][0] - prices[i]
            
            # if we sell on day n, we have to have bought on either days (0, ..., n-1)
            dp[i][2] = bought + prices[i]
            
            # keep track of the "max bought from the past"
            bought = max(bought, dp[i][1])
                    
        # return if we rest or sell on the last day
        return max(dp[n-1][0], dp[n-1][2])

# @lc code=end

