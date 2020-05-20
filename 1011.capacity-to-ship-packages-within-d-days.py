#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        # key: use bsearch 
        
        l, r = max(weights), sum(weights)

        # mid is current capacity
        while l < r:
             
            mid, day_need, curr = (l + r) // 2, 1, 0  

            for w in weights:
                # if curr + w > current capacity need additional day
                if curr + w > mid:
                    day_need += 1
                    curr = 0
                curr += w

            if day_need > D: l = mid + 1
            else: r = mid
        return l

# @lc code=end

