#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if stack and ch == stack[-1]:
                stack.pop()
            else:   
                stack.append(ch) 
        return "".join(stack)
# @lc code=end

