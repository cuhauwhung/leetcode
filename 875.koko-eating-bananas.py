#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        import math 
        
        # key: use bsearch to find the optimal hours Koko has to eat 
        #      use ceiling, because if p < m, we just count as 1 hour
        
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum(math.ceil(p/m) for p in piles) > H: 
                l = m + 1
            else: 
                r = m
        return l


# @lc code=end