#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = list()
        for i in s:
            if i.isalnum():
                ans.append(i.lower())
        if ans == ans[::-1]: return True
        return False 
# @lc code=end

