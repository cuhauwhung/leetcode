#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # key: use DP 
        #      f(0) = nums[0]
        #      f(1) = max(num[0], num[1])
        #      f(k) = max( f(k-2) + nums[k], f(k-1) )

        """ 
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1] # return the last element
        """        

        prev = curr = 0 
        for num in nums:
            temp, prev = prev, curr             # temp:= dp[i-2]th and prev:= dp[i-1]th
            curr = max(num + temp, prev)        # just plug into formula
        return curr 
    

        
# @lc code=end

