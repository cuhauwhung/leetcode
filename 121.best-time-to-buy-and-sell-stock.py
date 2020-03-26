#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # key:  kadane's algorithm
        #       does adding one more variable increase the sum 
        #       if yes, then update it, if not start with 0     

        # max_local, max_global = 0, 0
        # for i in range(1, len(prices)):
        #     max_local = max(0, max_local + prices[i] - prices[i-1])
        #     max_global = max(max_local, max_global)
        # return max_global

        # key: find max peak and min valley and get the difference 
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

# @lc code=end