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
                second_j = j + cycle - (2*i)                
                if i != 0 and i != numRows - 1 and second_j < len(s):
                    res += s[second_j]
        return res 
        
# @lc code=end