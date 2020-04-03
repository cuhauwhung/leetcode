#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
            return 
        else:
            current_min = self.stack[-1][1]
            self.stack.append((x, min(x, current_min)))

    def pop(self) -> None:
        self.stack.pop()
                              
    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# @lc code=end