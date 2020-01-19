#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root: return
        self.flatten(root.left)
        self.flatten(root.right)

        # move the left branch to the right 
        # and then go the bottom most of the "just moved" right 
        # and append previous right to the bottom most "just moved"

        if root.left:

            temp = root.right
            root.right = root.left
            root.left = None

            while root.right:
                root = root.right
                
            root.right = temp

# @lc code=end

