#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        if not M: return 0
        s = len(M)
        seen = set()
        
        def dfs(p):
            for q, adj in enumerate(M[p]):
                if (adj == 1) and (q not in seen):
                    seen.add(q)
                    dfs(q)
        
        count = 0
        for i in range(s):
            if i not in seen: 
                dfs(i)
                count += 1
        
        return count


# @lc code=end

