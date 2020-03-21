#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # key: Use sliding window to extend right, but if cum_sum >= k, start 
        # increasing left until cum_sum < k, then add to the count. 
        # if the range of values work, then every subset would work

        left = count = 0 
        cum_sum = 1 

        for right, val in enumerate(nums):
            cum_sum *= val 
            while left <= right and cum_sum >= k:
                cum_sum /= nums[left]
                left += 1 
            
            if cum_sum < k:
                count += right - left + 1 
                    
        return count 
# @lc code=end

