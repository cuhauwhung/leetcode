#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1: return s

        cycle = numRows * 2 - 2 
        res = ""

        for i in range(numRows):
            for j in range(i, len(s), cycle):
                res += s[j]
                secondJ = (j - i) + cycle - i
                if (secondJ-j) % cycle != 0 and secondJ < len(s):
                    res += s[secondJ]
        return res

# @lc code=end