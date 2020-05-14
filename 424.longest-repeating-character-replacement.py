#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # key: use sliding window 

        from collections import Counter
        counts = Counter()
        left = res = 0 

        for right in range(len(s)):
            counts[s[right]] += 1
            max_count = counts.most_common(1)[0][1]
            if right - left + 1 - max_count > k:
                counts[s[left]] -= 1
                left += 1 
            
            res = max(res, right - left + 1)

        return res 




# @lc code=end