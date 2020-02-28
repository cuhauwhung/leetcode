#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return 
        
        if key > root.val: 
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # key is the root of subtree
        else:

            # if the subtree does not have a left child, we just return its right child to its father, and they will be connected on the higher level recursion
            if not root.left:
                return root.right

            # if it has a left child, we want to find the max val on the left subtree to  replace the node we want to delete.
            else:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right

                root.val = tmp.val

                # don't want to keep tmp on subtree, so we delete it
                root.left = self.deleteNode(root.left, tmp.val)
                
        return root

# @lc code=end