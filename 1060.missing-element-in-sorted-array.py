#
# @lc app=leetcode id=1060 lang=python3
# [1060] Missing Element in Sorted Array
#

# @lc code=start
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        # idea: diff between physical length and value length

        def missCount(nums, mid):
            return nums[mid] - nums[0] - mid
        
        n = len(nums)
        if nums[n-1] - nums[0] - (n - 1 - 0) < k:
            return nums[n-1] + k - missCount(nums, n - 1)

        l, r = 0, n - 1 
        while l < r:
            mid = l + (r - l) // 2
            if missCount(nums, mid) < k:
                l = mid + 1 
            else:
                r = mid 
        
        return nums[l - 1] + k - missCount(nums, l - 1)





# @lc code=end