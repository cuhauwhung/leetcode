#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        list_s = list(s)
        stack = list()

        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            if char == ")":
                if len(stack) > 0:
                    _ = stack.pop()
                else:
                    list_s[idx] = "#"
                    
        while stack: list_s[stack.pop()] = "#"
        return "".join([c for c in list_s if c != "#"])
# @lc code=end

