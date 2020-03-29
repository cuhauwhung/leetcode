#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # key: use DP
        #      dp[i] = how many ways to make up cur_amount 
        #              with coins we have so far. 
        #              - When cur_coin == cur_amount, it has to refer back to dp[0] = 1
        
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for cur_coin in coins:
            for cur_amount in range(1, amount + 1):
                if cur_amount >= cur_coin:
                    dp[cur_amount] += dp[cur_amount - cur_coin]
        return dp[amount]
    
    