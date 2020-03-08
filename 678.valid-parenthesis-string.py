#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:

        # key: 
        # cmax: counts the max open paren, max number of unbalanced "(" that COULD be paired 
        # cmin: counts the min open paren, max number of unbalance "(" that MUST be paired

        cmin = cmax = 0 
        for c in s:
            if c == "(":
                cmin += 1 
                cmax += 1 
            
            if c == ")":
                cmax -= 1
                cmin = max(cmin - 1, 0)
            
            if c == "*":
                cmax += 1
                cmin = max(cmin - 1, 0)

            if cmax < 0: return False
        
        return cmin == 0

# @lc code=end