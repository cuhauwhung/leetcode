#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque

        start = ([0],[])
        to_visit = deque([start])
        res = []
        
        while to_visit:
            nxt, path = to_visit.popleft()
            
            for cur in nxt:
                to_visit.append((graph[cur], path + [cur]))
            
            if not nxt:
                res.append(path)
                
        return res 
# @lc code=end

