#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        

        # key: use BFS
        #      make graph and start from the leaves. Keep eating away the leaves until we reach the middle
        #      the middle would be the best root
        #      there can only be 1 or 2 roots 

        if n == 1: return [0]
        adj = [set() for _ in range(n)]
        for i, j in edges: 
            adj[i].add(j)
            adj[j].add(i)
        
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = list()

            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: newLeaves.append(j)
            leaves = newLeaves

        return leaves 
        
# @lc code=end