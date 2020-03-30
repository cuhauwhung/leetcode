#
# @lc app=leetcode id=1055 lang=python3
#
# [1055] Shortest Way to Form String
#

# @lc code=start
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        from collections import defaultdict

        # key: similar to 792. 
        #      Create mapping of indexes then perform binary search for index
        #      while keeping track of the index at source, if at end start again  
        
        
        mapping = defaultdict(list)
        for i, c in enumerate(source):
            mapping[c].append(i)

        # i == smallest valid next index 
        count, i = 1, -1 
        for c in target:

            if c not in mapping: return -1 
            char_idxs = mapping[c]

            # index in char_idxs that is >= i 
            search_idx = bisect.bisect_left(char_idxs, i)

            if search_idx == len(char_idxs):
                count += 1 
                i = char_idxs[0] + 1 
            
            else:
                i = char_idxs[search_idx] + 1    

        return count 


# @lc code=end

