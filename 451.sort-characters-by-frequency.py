#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        char_map = Counter(s)
        sort_freq = sorted(char_map.items(), key=lambda x: x[1], reverse=True)
        return ''.join(x[0]*x[1] for x in sort_freq)
# @lc code=end

