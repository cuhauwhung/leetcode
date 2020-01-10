#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()
        mappings = {"(": ")", "{":"}", "[": "]"}

        for this_char in s:
            
            # if opening bracket just append 
            if this_char in mappings: 
                stack.append(this_char)
            
            else: 
                # if stack is empty but there is closing 
                # or if the closing doesn't match the opening 
                if not stack or (stack.pop() != (list(mappings.keys())[list(mappings.values()).index(this_char)])):
                    return False 

        # stack still contains elements, then return false
        if len(stack) > 0:
            return False
                
        return True 

# @lc code=end


