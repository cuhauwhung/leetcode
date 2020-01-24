#
# @lc app=leetcode id=1131 lang=python3
#
# [1131] Maximum of Absolute Value Expression
#

# @lc code=start
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        
        # key idea: max difference between distances from each person to one corner 
        #           find furthest and closest person for each corner, take diff,and track the max difference

        ans, n = 0, len(arr1)
        for a, b in (1, 1), (1, -1), (-1, 1), (-1, -1):
            close = a * arr1[0] + b * arr2[0] + 0
            for i in range(n):
                curr = a * arr1[i] + b * arr2[i] + i 
                ans = max(ans, curr - close)
                close = min(close, curr)
        return ans

        
# @lc code=end
