#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # key: check if x is the start of the streak (x-1 not in set), then test y = x + 1, x + 2, x + 3 and find the first y not in the set 

        nums = set(nums)
        best = 0 

        for x in nums:
            if x - 1 not in nums:
                y = x + 1 
                while y in nums:
                    y += 1 
                best = max(best, y - x)
        return best 

# @lc code=end