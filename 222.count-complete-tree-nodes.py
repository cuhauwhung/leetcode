#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        hLeft = hRight = 0 
        pLeft = pRight = root 

        while pLeft:
            hLeft += 1 
            pLeft = pLeft.left

        while pRight:
            hRight += 1 
            pRight = pRight.right

        if hLeft == hRight:
            return (2 ** hLeft) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1 

        # # Linear time 
        # if not root: return 0
        # return self.countNodes(root.left) + self.countNodes(root.right) + 1 

        
# @lc code=end

