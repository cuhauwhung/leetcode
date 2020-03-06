#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        res = list()
        
        def helper(root, parent_exist):
            
            if root is None:
                return None
            
            if root.val in to_delete:
                root.left = helper(root.left, parent_exist=False)
                root.right = helper(root.right, parent_exist=False)
                return None
            
            else:
                if not parent_exist:
                    res.append(root)
                root.left = helper(root.left, parent_exist=True)
                root.right = helper(root.right, parent_exist=True)
                return root
            
        helper(root, parent_exist=False)
        return res
 
# @lc code=end

