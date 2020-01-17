#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_val: int) -> List[List[int]]:

        # note: when dealing with trees we have to append twice and pop twice
        def dfs(root, sum_val, curr, ans):

            if not root.left and not root.right and sum(curr) == sum_val:
                ans.append(curr[:])
                return 

            if root.left: 
                curr.append(root.left.val)
                dfs(root.left, sum_val, curr, ans)
                curr.pop()

            if root.right: 
                curr.append(root.right.val)
                dfs(root.right, sum_val, curr, ans)
                curr.pop()

        if not root: return []
        ans = list()
        dfs(root, sum_val, [root.val], ans)
        return ans 


# @lc code=end

