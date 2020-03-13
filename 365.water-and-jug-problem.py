#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # key: bezouts lemma, if x + y. For nonzero integers a and b, let d be the greatest common divisor 
        # d = \gcd(a,b)d=gcd(a,b). Then, there exist integers x and y such that ax + by = d.

        if z == 0: return True
        if x+y<z: return  False
        return z % math.gcd(x, y) == 0

# @lc code=end