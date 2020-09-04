#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        counts = Counter(nums)
        
        for k, v in counts.items():
            if v > 1:
                return True
        return False

# @lc code=end