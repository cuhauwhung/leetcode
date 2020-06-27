#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import defaultdict
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

        return res[:k]

# @lc code=end