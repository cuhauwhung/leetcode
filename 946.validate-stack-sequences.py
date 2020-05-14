#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        # key: append pushed values into stack and try to pop as many values as possible 
        #      if it is same as the current one of popped
        #      check if stack is empty at the end 
                
        stack = [] 
        i = 0 
        for x in pushed:
            stack.append(x)
            
            while stack and stack[-1] == popped[i]:
                i += 1 
                stack.pop()
                
        return len(stack) == 0

# @lc code=end