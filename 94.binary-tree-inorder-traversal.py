#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# (a + b)
# left root right 
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def traverse(root, ans):
            if not root:
                return 
            
            else: 
                traverse(root.left, ans)
                ans.append(root.val)
                traverse(root.right, ans)

        ans = list()
        traverse(root, ans)
        return ans 
        
# @lc code=end

