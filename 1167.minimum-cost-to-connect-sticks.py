#
# @lc app=leetcode id=1167 lang=python3
#
# [1167] Minimum Cost to Connect Sticks
#

# @lc code=start
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            res += x + y
            heapq.heappush(sticks, x + y)
        return res


# @lc code=end