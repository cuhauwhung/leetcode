#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
        
# @lc code=end

