#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0 
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1 
        return left 

# @lc code=end