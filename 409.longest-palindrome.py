#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter 
        ans, s_count = 0, Counter(s)

        for num, count in s_count.items():
            if count % 2 == 0 or ans % 2 == 0:
                ans += count
            else:
                ans += count - 1 
                
        return ans 

# @lc code=end

