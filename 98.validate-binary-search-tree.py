#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True
            if node.val >= upper or node.val <= lower:
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        return dfs(root, float('-inf'), float('inf'))
        
# @lc code=end
