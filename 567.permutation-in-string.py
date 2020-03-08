#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        # key: similar to 438 (Find all anagrams in a string)

        dict_1 = Counter(s1)
        dict_2 = Counter(s2[:len(s1)])
        i, j = 0, len(s1) 
        
        while j <= len(s2):
            
            if dict_1 == dict_2:
                return True 
            
            dict_2[s2[i]] -= 1
            if dict_2[s2[i]] <= 0:
                dict_2.pop(s2[i])
            
            if j < len(s2):
                dict_2[s2[j]] += 1
            
            i += 1 
            j += 1
        
        return False 
# @lc code=end

