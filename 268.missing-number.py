#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # key: Sum of 0..n minus sum of the given numbers is the missing one
        n = len(nums)
        return (n * (n+1) // 2) - sum(nums)

# @lc code=end