#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # idea:
        #       does adding one more variable increase the sum 
        #       if yes, then update it
        #       then check if this new local variable is greater than the global variable 
        max_global = max_local = nums[0]
        
        for x in nums[1:]:
            max_local = max(x, max_local +  x)
            max_global = max(max_global, max_local)
            
        return max_global

# @lc code=end

