#
# @lc app=leetcode id=742 lang=python3
#
# [742] Closest Leaf in a Binary Tree
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:

        # key: use dfs to find the graph and the leaves
        #      then use bfs to find closest leaf to k  

        from collections import defaultdict
        
        graph = defaultdict(list)
        leaves = set()
        
        def traverse(root):
            
            if not root:
                return
           
            if not root.left and not root.right:
                leaves.add(root.val)
        
            if root.left:
                graph[root.left.val].append(root.val)
                graph[root.val].append(root.left.val)
                traverse(root.left)
                
            if root.right:
                graph[root.right.val].append(root.val)
                graph[root.val].append(root.right.val)
                traverse(root.right)
            
        traverse(root)
        
        queue = [k]
        while queue:
            next_queue = []
            for node in queue:
                if node in leaves:
                    return node
                next_queue += graph.pop(node, ())
            queue = next_queue

# @lc code=end
