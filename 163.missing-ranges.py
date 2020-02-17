#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        # idea: different between two positions has to be exactly or greater than 2 

        ans = list()
        nums = [lower-1] + nums + [upper+1]

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                ans.append(str(nums[i]+1))
            if nums[i+1] - nums[i] > 2:
                ans.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        return ans

