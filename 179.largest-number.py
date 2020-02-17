#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools 

        def custom_func(x1, x2):
            if x1 + x2 > x2 + x1: return -1 
            elif x1 + x2 < x2 + x1: return 1 
            else: return 0

        if not any(nums): return "0"
        return "".join(sorted(map(str, nums), key=functools.cmp_to_key(custom_func)))

# @lc code=end
