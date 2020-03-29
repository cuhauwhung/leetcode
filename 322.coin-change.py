#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins, amount):

        # key: use DP 
        #      dp[i] = # of ways we can make change of this amount 
        #              with current_coin

        dp = [amount+1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                # if this_count is less than the amount, we can perform DP
                if c <= i: 
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return -1 if dp[amount] == amount+1 else dp[amount]  

        # # DFS + Greedy + Pruning solution
        # self.ans = float('Inf')
        # def dfs(s, amount, curr_count):
        #     if amount == 0:
        #         self.ans = curr_count 
        #         return 

        #     # prevent from accessing coins[s+1], which will result in index out of range 
        #     if s == len(coins): 
        #         return             
        #     coin = coins[s]
            
        #     # essentially we reduce the search space, by targeting the big coins first 
        #     # and removing the big coins from amount. If what we are going to add into the 
        #     # coin pouch is greater than what we already have, then just break, there's no point 
        #     # in testing this DFS path
        #     for k in range(amount // coin, -1, -1):
        #         if curr_count + k >= self.ans:
        #             break 
        #         dfs(s + 1, amount - (k * coin), curr_count + k)
        
        # coins.sort(reverse=True)
        # dfs(0, amount, 0)
        # return -1 if self.ans == float('Inf') else self.ans   

# KEY: we can't test out all possible paths, because there will be path explosion, we have to prune the search space first!
# @lc code=end

