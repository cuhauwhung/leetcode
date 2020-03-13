#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # key: at each node, we have 2 options: rob or not rob 
    def rob(self, root: TreeNode) -> int:
        res = self.robSub(root)

        return max(res)

    def robSub(self, root):
        res = [0, 0]
        if not root: return res
        left = self.robSub(root.left)
        right = self.robSub(root.right)

        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]

        print(root.val, res)
        return res 

# @lc code=end

