#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # key: neighbors at each level will be a different color
        #       call DFS on self and then neighbors and keep track # of colors 

        color = dict()
        def dfs(pos):
            for nei in graph[pos]:
                if nei in color:
                    if color[pos] == color[nei]:
                        return False
                else:
                    color[nei] = 1 - color[pos]
                    if not dfs(nei):
                        return False
            return True 

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0 
                if not dfs(i):
                    return False
        return True 

# @lc code=end