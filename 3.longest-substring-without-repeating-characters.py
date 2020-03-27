#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        left, right, n = 0, 0, len(s)
        seen = set()
        while left < n and right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                seen.remove(s[left])
                left += 1
        return longest

# @lc code=end