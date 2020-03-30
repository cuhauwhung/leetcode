#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        # key:
        #           1) keep running sum and add 
        #           2) if total_sum is more than s, then we have to move the start forward

        total_sum, start = 0, 0
        min_length = float("Inf")

        for end in range(len(nums)):

            total_sum += nums[end]
            
            while total_sum >= s:
                min_length = min(min_length, end - start + 1)
                total_sum -= nums[start]
                start += 1

        return min_length if min_length != float("Inf") else 0 



# @lc code=end

