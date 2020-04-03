#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right
        
        
# @lc code=end