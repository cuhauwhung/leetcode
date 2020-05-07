#
# @lc app=leetcode id=1060 lang=python3
# [1060] Missing Element in Sorted Array
#

# @lc code=start
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        # use bsearch
        l, r = 0, len(nums) - 1
        
        while l < r:

            mid = (l+r+1) // 2

            #count the number of missing from the begining to mid point
            if nums[mid] - nums[0] - mid < k:
                l = mid

            else:
                r = mid -1

        # first val + kth missing num + left index of range
        return nums[0] + k + l

# @lc code=end
