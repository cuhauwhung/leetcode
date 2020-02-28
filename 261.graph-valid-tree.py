#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        
        if len(edges) != n - 1: return False
        nodes_map = defaultdict(list)
        for e in edges:
            nodes_map[e[0]].append(e[1])
            nodes_map[e[1]].append(e[0])
        
        # use bfs to go through the nodes
        queue = [0]
        seen = {0}
        
        while queue:
            curr = queue.pop(0)
                    
            for nei in nodes_map[curr]:
                if nei not in seen:
                    queue.append(nei)
                    seen.add(nei)
        return len(seen) == n
        
# @lc code=end