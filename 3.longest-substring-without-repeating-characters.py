#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0 
        output = 0 

        for r in range(len(s)):
            
            # never seen so keep increasing window on right 
            if s[r] not in seen:
                output = max(output, r - l + 1)
            else:
                # not inside current window, can keep increaseing window on right 
                if seen[s[r]] < l:
                    output = max(output, r - l + 1)

                # inside current window, so can't repeat so move l to new position (one right of where the same letter was seen)
                else:
                    l = seen[s[r]] + 1 

            seen[s[r]] = r 

        return output 
        
# @lc code=end

