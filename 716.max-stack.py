#
# @lc app=leetcode id=716 lang=python3
#
# [716] Max Stack
#

# @lc code=start
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        self.stack = self.stack[::-1]
        max_num = self.stack.pop(self.stack.index(max(self.stack)))
        self.stack = self.stack[::-1]
        return max_num
    
# @lc code=end

