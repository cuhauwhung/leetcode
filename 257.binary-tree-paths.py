#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def dfs(root, curr, res):

            if not root.left and not root.right:
                res.append(curr + str(root.val))

            if root.left:
                dfs(root.left, curr + str(root.val) + "->", res)
                
            if root.right:
                dfs(root.right, curr + str(root.val) + "->", res)

        if not root: return []
        ans = list()
        dfs(root, "", ans)
        return ans 


# @lc code=end

