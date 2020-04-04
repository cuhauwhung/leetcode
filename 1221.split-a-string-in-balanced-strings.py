#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = count = 0
        for c in s:
            count += 1 if c == 'L' else -1 
            if count == 0:
                res += 1
        return res 

# @lc code=end