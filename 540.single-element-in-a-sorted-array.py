#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # key: use XOR with 1 to find "partner index"
        #      if odd: partner = index - 1 
        #      if even: partner = index + 1 
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
        
# @lc code=end