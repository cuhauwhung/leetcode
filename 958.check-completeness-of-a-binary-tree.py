#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:

        nodes = [root]
        i = 0
        while nodes[i]:
            node = nodes[i]
            i += 1 
            nodes.append(node.left)
            nodes.append(node.right)
         
        # For a complete binary tree, there 
        # should not be any node after we meet an empty one.
        return not any(nodes[i:]) 
# @lc code=end

