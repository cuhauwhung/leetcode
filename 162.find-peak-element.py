#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # o(n) solution
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         return i 
        # return len(nums) - 1

        # key: use bsearch: o(log n) 
        l, r = 0, len(nums)-1
        while l < r: 
            mid = l + (r-l)//2
            if nums[mid] > nums[mid+1]:
                r = mid 
            else: 
                l = mid + 1 
        return l 


# @lc code=end

