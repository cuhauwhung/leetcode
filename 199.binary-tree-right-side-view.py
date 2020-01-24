#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        from collections import deque

        result = list()
        if not root: return result
        
        q = deque()
        q.append(root)

        while q:

            nodes_at_height = len(q)

            for i in range(nodes_at_height):
                curr_node = q.popleft()

                if i == nodes_at_height - 1:
                    result.append(curr_node.val)
                
                if curr_node.left: q.append(curr_node.left)
                if curr_node.right: q.append(curr_node.right)

        return result

            

# @lc code=end

