#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root) != -1

        
    def helper(self, curr): 
        
        if curr is None: return 0
        left = self.helper(curr.left)
        right = self.helper(curr.right) 
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
            
        return max(left, right) + 1 



# @lc code=end
