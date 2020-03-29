#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # key: group nums based on regions red, white, and blue 
        # depending on what white ptr is, we perform swaps 
        # if white is 0, we swap with red
        # if white is 1, correct so don't move 
        # if white is 2, swap with blue 

        red, white, blue = 0, 0, len(nums) - 1 
    
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1 
                white+= 1 

            elif nums[white] == 1:
                white += 1 

            else:
                nums[white], nums[blue] = nums[blue], nums[white] 
                blue -= 1 

# @lc code=end