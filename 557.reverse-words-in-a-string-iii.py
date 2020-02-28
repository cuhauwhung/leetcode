#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        parsed = s.strip().split(" ")
        parsed = [x[::-1] for x in parsed]
        return " ".join(parsed) 
# @lc code=end

