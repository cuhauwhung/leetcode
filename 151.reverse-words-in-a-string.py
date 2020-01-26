#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        rev_s = s.strip().split()[::-1]
        return " ".join(rev_s) 
# @lc code=end

