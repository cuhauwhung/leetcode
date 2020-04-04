#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # key: use stack to remove larger digits 
        
        stack = list()
        for digit in num:
            
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1 
            stack.append(digit)
            
        stack = stack[:-k] if k else stack
        return "".join(stack).lstrip('0') or "0"

# @lc code=end