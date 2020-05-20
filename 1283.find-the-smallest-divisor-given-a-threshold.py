#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        # key: use bsearch
        #      (n + divisor - 1) / divisor is the same as ceiling
        #      if sum > threshold, divisor is too small, so increase left bound 
        #      else divisor is too big, so divisor becomes right bound  

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2 
            if sum((x + mid - 1) // mid for x in nums) > threshold:
                left = mid + 1 
            else:
                right = mid 

        return left 

# @lc code=end

