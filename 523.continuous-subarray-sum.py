#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        tot_sum = 0 
        this_dict = {0: -1}

        for i in range(len(nums)):
            tot_sum += nums[i]
            
            if (k != 0):
                tot_sum = tot_sum % k 
                
            if tot_sum in this_dict: 
                if i - this_dict[tot_sum] > 1:
                    return True 
            else:
                this_dict[tot_sum] = i
                    
        return False
# @lc code=end

