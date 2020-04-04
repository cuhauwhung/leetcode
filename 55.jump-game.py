#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # key: m = maximum distance we can reach so far 
        
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True 
# @lc code=end

