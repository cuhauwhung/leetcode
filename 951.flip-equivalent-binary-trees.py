#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
                
        # key: recurisvely return false only if root1.val != root2.val
        #      the children of each root should be the same or flipped 
        
        if not root1 or not root2:
            return root1 is root2 
        
        if root1.val != root2.val:
            return False 
        
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) 
                or (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)))
        
# @lc code=end

