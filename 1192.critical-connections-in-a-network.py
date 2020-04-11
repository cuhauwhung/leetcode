#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict 

        # key: we have to detect cycle by using rank. Find the smallest rank returned by 
        #      neighbor and remove that 
        #
        #      time: O(|E|)
        #      space: O(graph) + O(rank) + O(connections) = 3 * O(|E| + |V|) = O(|E|)

        def makeGraph(connections):
            graph = defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph

        graph = makeGraph(connections)
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n

        def dfs(node, depth):
            
            # visiting (0<=rank<n), or visited (rank=n)
            if rank[node] >= 0:
                return rank[node]

            rank[node] = depth 
            min_back_depth = n 
            for nei in graph[node]:
                
                # don't re-visit nodes we came from 
                if rank[nei] == depth - 1:
                    continue 
                
                back_depth = dfs(nei, depth + 1) 

                # there is a loop 
                if back_depth <= depth: 
                    connections.discard(tuple(sorted((nei, node))))

                min_back_depth = min(min_back_depth, back_depth)
                
            return min_back_depth  

        dfs(0, 0)
        return list(connections)

# @lc code=end