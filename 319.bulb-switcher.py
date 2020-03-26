#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
class Solution:
    def bulbSwitch(self, n: int) -> int:
    
        # key: 
        # i  bulbs    
        # 1  1
        # 2  10 
        # 3  100 
        # 4  1001 
        # 5  10010
        # 6  100100
        # 7  1001000
        # 8  1001000
        # 9  100100001

        return int(math.sqrt(n))
# @lc code=end

