#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # key: use DP
        #      dp[i] is the max number of points in [minimum, i]. 
        #      Then we have dp[i] = max(dp[i-2] + dic[i] * i, dp[i-1])

        from collections import Counter
        if not nums: return 0        
        my_counter = Counter(nums)
        maximum = max(my_counter.keys())
        minimum = min(my_counter.keys())
        
        prev, curr = 0, 0
        for i in range(minimum, maximum+1):
            prev, curr = curr, max(prev + my_counter[i]*i, curr)
            
        return curr

# @lc code=end