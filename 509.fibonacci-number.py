#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        
        # iterative 
        # if not N: return 0
        # fibs = [0, 1]
        # for i in range(1, N):
        #     x1, x2 = fibs[i-1], fibs[i]
        #     fibs.append(x1+x2)
        # return fibs[-1]

        # recursive 
        if N == 0: return 0
        if N == 1: return 1 
        return self.fib(N-1) + self.fib(N-2)

# @lc code=end

