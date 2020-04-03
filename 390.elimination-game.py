#
# @lc app=leetcode id=390 lang=python3
#
# [390] Elimination Game
#

# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        # arr = range(1, n+1)
        # while len(arr) > 1:
        #     arr = arr[1::2][::-1]
        # return arr[0]
        return self.leftToRight(n)

    # O(log n)
    # key: eliminate [1...n] first from left to right, then alternate
    def leftToRight(self, n):
        if n == 1: return 1 

        # scan from left to right is simple, the length of array doesn't matter
        # [1, 2, 3, 4] -> 2 * [1, 2]
        # [1, 2, 3, 4, 5] -> 2 * [1, 2]
        return 2 * self.rightToLeft(n//2)
        
    def rightToLeft(self, n):
        if n == 1: return 1 
        
        # if the length of array is even, we will get only odd number
        # [1, 2, 3, 4] -> [1, 3] = 2 * [1, 2] - 1
        if n % 2 == 0: return 2 * self.leftToRight(n//2) - 1
        
        # else if the length of array is odd, we will get only even number
        # [1, 2, 3, 4, 5] -> [2, 4] = 2 * [1, 2]
        else: return 2 * self.leftToRight(n//2)
        

# @lc code=end