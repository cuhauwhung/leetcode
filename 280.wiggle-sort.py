#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort 
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:

        # key: just go through each element and check if property is satisfied 
        # if not, perform swap 
                
        """
        Do not return anything, modify nums in-place instead.
        """ 
        for i in range(len(nums)-1):
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

# @lc code=end