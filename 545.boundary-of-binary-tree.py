#
# @lc app=leetcode id=545 lang=python3
#
# [545] Boundary of Binary Tree
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:

        # key: use different traversal methods to find the different boundaries 

        # pre-order traversal 
        def dfs_leftmost(node):
            if not node or not node.left and not node.right: 
                return 
            boundary.append(node.val)
            if node.left: dfs_leftmost(node.left)
            else: dfs_leftmost(node.right)
        
        # in order traversal
        def dfs_leaves(node):
            if not node: 
                return 
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right: 
                boundary.append(node.val)
            dfs_leaves(node.right)

        # post order traversal 
        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return 
            if node.right: dfs_rightmost(node.right)
            else: dfs_rightmost(node.left)
            boundary.append(node.val) 

        if not root: return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary


# @lc code=end

