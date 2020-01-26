#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        # make graph using dfs
        conn = defaultdict(list)
        def make_graph(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: make_graph(child, child.left)
            if child.right: make_graph(child, child.right)
        
        make_graph(None, root)


        # use dfs to find graph at level k 
        seen = set()
        queue = [target.val]

        for _ in range(K):
            size, level = len(queue), []

            for _ in range(size):

                cur = queue.pop()

                if cur not in seen:
                    level += conn.get(cur, [])
                    seen.add(cur)

            queue = level     
        return [x for x in queue if x not in seen]
 
# @lc code=end

