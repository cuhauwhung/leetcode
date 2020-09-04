#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        def simple_rob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        
        return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

# @lc code=end