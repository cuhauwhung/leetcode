#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Idea: we go left to right multiply then back to right 
        #       L[i] = L[i-1] * nums[i-1], where L[0] = 1
        #       same intuition going back from right -> left  
        #       then we just multiple L[i] * R[i]

        p = 1 
        output = list()
        for i in range(0, len(nums)):
            output.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output

# @lc code=end

