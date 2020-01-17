#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    # idea: keep looping and keep calling digit square. If seen return false, if not seen then keep going 

    def isHappy(self, n: int) -> bool:
        seen = set()
        current = n
        while current != 1:
            current = self.digit_square(current)
            if current in seen: return False
            seen.add(current)
        return True 

    def digit_square(self, num):
        base = 1 
        result = 0 
        while num % base < num: 
            digit = (num // base) % 10
            result += digit * digit 
            base *= 10
        return result 

# @lc code=end

