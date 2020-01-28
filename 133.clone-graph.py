#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import defaultdict


        if not node: return node

        visited = dict()

        queue = [node]
        visited[node] = Node(node.val, [])

        while queue:
            n = queue.pop(0)

            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                    
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]









# @lc code=end

