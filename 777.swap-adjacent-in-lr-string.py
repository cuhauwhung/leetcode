#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        # key: only R can go right and L can go left
        # we store the index of both start and end and check if 
        # the indexes are valid  
        
        if len(start) != len(end): return False
        A = [(s, idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
        B = [(e, idx) for idx, e in enumerate(end) if e == 'L' or e == 'R']
        if len(A) != len(B): return False
                
        for (s, i), (e, j) in zip(A, B):
            if s != e: return False
            
            if s == 'L':
                if i < j:
                    return False
                    
            if s == 'R':
                if i > j:
                    return False
        return True 

# @lc code=end

