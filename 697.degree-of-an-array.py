#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        from collections import defaultdict
        nums_map = defaultdict(list)
        deg = 0 
        min_len = float('Inf')

        for i, num in enumerate(nums):
            nums_map[num].append(i)
            deg = max(deg, len(nums_map[num]))

        for num, indices in nums_map.items():
            if len(indices) == deg:
                min_len = min(min_len, indices[-1] - indices[0] + 1)
        
        return min_len 

# @lc code=end