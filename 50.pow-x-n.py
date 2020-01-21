#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0: return 1 
        if n < 0: return 1 / self.myPow(x, -n)
        if n % 2: return x * self.myPow(x, n - 1) # n is odd 
        return self.myPow(x * x, n/2) # n is even
        
# @lc code=end

