#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter     

        # key: use sliding window. 
        #      use a separate variable counts to keep track if we are 
        #      in the "desired" window space. If we are, then move left

        hashmap = Counter(t)
        counts = len(t)

        min_window = "" 
        left = 0 

        for right, char in enumerate(s):
            if hashmap[char] > 0:
                counts -= 1 
            hashmap[char] -= 1

            while counts == 0:
                length = right - left + 1 
                if not min_window or len(min_window) > length: 
                    min_window = s[left:right+1]

                hashmap[s[left]] += 1 
                if hashmap[s[left]] > 0:
                    counts += 1 
                
                left += 1

        return min_window 
        
# @lc code=end

