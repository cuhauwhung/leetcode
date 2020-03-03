#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        table = {0: 0} 
        max_length = 0 

        for ind, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1 

            if count in table:
                max_length = max(max_length, ind - table[count])
            else:
                table[count] = ind

        return max_length


# @lc code=end