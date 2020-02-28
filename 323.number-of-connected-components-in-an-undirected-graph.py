#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        def dfs(curr):
            if curr in visited: return 
            visited.add(curr)
            for nei in nodes_map[curr]:
                dfs(nei)
            
        count = 0 
        visited = set()
        nodes_map = defaultdict(list)
        for e in edges:
            nodes_map[e[0]].append(e[1])
            nodes_map[e[1]].append(e[0])
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count 
        
# @lc code=end