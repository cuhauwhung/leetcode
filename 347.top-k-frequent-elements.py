#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = list(Counter(nums).most_common(k))
        ans = [x[0] for x in ans]
        return ans 

# @lc code=end

