#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        # self.res = None
        # self.dfs(root, p)
        # return self.res
        
        # def dfs(self, root, p):
        #     if not root: return
        #     if p.val < root.val:
        #         self.res = root
        #         self.dfs(root.left, p)
        #     else:
        #         self.dfs(root.right, p)

        # curr = root
        # candidate = None

        # while curr:
        #     if curr.val > p.val:
        #         candidate = curr 
        #         curr = curr.left
        #     else:
        #         curr = curr.right
        # return candidate

        if not root: return
        curr = root
        stack = []
        prev = None 

        while stack or curr: 
            if curr: 
                stack.append(curr)
                curr = curr.left

            else:

                last = stack.pop()
                if last == p:
                    prev = last

                elif prev:
                    return last

                curr = last.right
        return 


# @lc code=end