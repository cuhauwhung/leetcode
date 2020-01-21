#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # key idea: we only want to increase as little as possible 
        #           go from right to left and then find point where the increasing trend is broken
        #           swap this value with the smallest possible number
        #           reverse the suffix

        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        # nums are in descneding order, so reverse and return 
        if i == 0:  
            nums.reverse()
            return 

        # find the last "ascending position"
        while nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]  
        nums[i : len(nums)] = nums[i : len(nums)][::-1]
        
# @lc code=end

