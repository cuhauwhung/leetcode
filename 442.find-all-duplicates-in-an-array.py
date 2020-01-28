#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:



        # key idea: when find a number i, flip the number at position i-1 to negative. 
        #           if the number at position i-1 is already negative, i is the number that
        #           occurs twice.

        L = len(nums)
        for i in range(L):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

            else:
                nums.append(abs(nums[i]))

        return nums[L:]

# @lc code=end