#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ans, i, j = list(), 0, len(p)
        p_dict = Counter(p)
        s_dict  = Counter(s[:len(p)])
        
        while j <= len(s):

            if p_dict == s_dict:
                ans.append(i)

            s_dict[s[i]]-=1
            if s_dict[s[i]] <= 0:
                s_dict.pop(s[i])
                
            if j < len(s):    
                 s_dict[s[j]] += 1
            
            j+=1
            i+=1
            
        return ans    

# @lc code=end

