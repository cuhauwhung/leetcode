#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return root

        queue, res = [], []
        queue.append(root)

        while queue:

            ans = []
            l = len(queue)

            for l in range(l):
                node = queue.pop(0)
                ans.append(node.val)

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                    
            res.append(ans)

        return res



# @lc code=end

