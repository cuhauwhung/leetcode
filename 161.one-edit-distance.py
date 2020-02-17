#
# @lc app=leetcode id=161 lang=python3
#
# [161] One Edit Distance
#

# @lc code=start
class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # key: insertion and deletion is the reversed
        
        l1, l2 = len(s), len(t)
        if l1 > l2: return self.isOneEditDistance(t, s)
        if s == t or l2 - l1 > 1: return False
        
        for i in range(len(s)):
            if s[i] != t[i]:
                if l1 == l2:
                    s = s[:i]+t[i]+s[i+1:]  # replacement
                else:
                    s = s[:i]+t[i]+s[i:]  # insertion
                break
        
        return s == t or s == t[:-1]
        
# @lc code=end

